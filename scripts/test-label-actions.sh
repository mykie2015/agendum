#!/usr/bin/env bash
# Label workflow cases:
# 1. type WATCH, body contains "BUILD READ P0" -> watch only
# 2. type READ, body contains "README" -> read, and README is not a type
# 3. priority P1, with P0 later in the body -> p1
# Also: unknown values are logged and skipped; edits drop conflicting
# type/priority labels and keep topic labels.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 - <<'PY'
import re
import sys
from pathlib import Path

import yaml

errors = []

def fail(msg):
    errors.append(msg)

form_path = Path(".github/ISSUE_TEMPLATE/action.yml")
workflow_path = Path(".github/workflows/label-actions.yml")
labels_path = Path(".github/ISSUE_LABELS.md")
readme_path = Path("README.md")
skeleton_path = Path("docs/issue-body-skeleton.md")

form = yaml.safe_load(form_path.read_text())
workflow = yaml.safe_load(workflow_path.read_text())
labels_md = labels_path.read_text()
readme = readme_path.read_text()
skeleton = skeleton_path.read_text()

if not isinstance(form, dict):
    fail("issue form is not a mapping")
    form = {}

for key in ("name", "description", "body"):
    if not form.get(key):
        fail(f"issue form missing {key}")

allowed_top = {"name", "description", "body", "title", "labels", "assignees", "projects"}
for key in form:
    if key not in allowed_top:
        fail(f"issue form has unknown top-level key {key}")

if not isinstance(form.get("title"), str) or "[TYPE]" not in form.get("title", ""):
    fail("issue form title must follow [TYPE] YYYY-MM-DD · decision")

if form.get("labels") != ["action"]:
    fail(f"issue form labels must be exactly ['action'], got {form.get('labels')}")

allowed_types = {"markdown", "input", "textarea", "dropdown", "checkboxes"}
attr_keys = {
    "markdown": {"value"},
    "input": {"label", "description", "placeholder", "value"},
    "textarea": {"label", "description", "placeholder", "value", "render"},
    "dropdown": {"label", "description", "multiple", "options", "default"},
    "checkboxes": {"label", "description", "options"},
}
id_re = re.compile(r"^[A-Za-z0-9_-]+$")
ids = []
field_labels = []
body = form.get("body") or []
if not isinstance(body, list) or not body:
    fail("issue form body must be a non-empty list")

for index, item in enumerate(body):
    if not isinstance(item, dict):
        fail(f"body[{index}] is not a mapping")
        continue
    item_type = item.get("type")
    if item_type not in allowed_types:
        fail(f"body[{index}] has invalid type {item_type!r}")
        continue
    unknown = set(item) - {"type", "id", "attributes", "validations"}
    if unknown:
        fail(f"body[{index}] has unknown keys {sorted(unknown)}")
    attributes = item.get("attributes")
    if not isinstance(attributes, dict):
        fail(f"body[{index}] missing attributes")
        attributes = {}
    extra_attr = set(attributes) - attr_keys[item_type]
    if extra_attr:
        fail(f"body[{index}] {item_type} has unknown attributes {sorted(extra_attr)}")
    if item_type != "markdown":
        item_id = item.get("id")
        if not isinstance(item_id, str) or not id_re.fullmatch(item_id):
            fail(f"body[{index}] id is missing or invalid: {item_id!r}")
        else:
            ids.append(item_id)
        label = attributes.get("label")
        if not isinstance(label, str) or not label.strip():
            fail(f"body[{index}] label is missing")
        else:
            field_labels.append(label)
    else:
        if "id" in item:
            fail("markdown intro should not have an id")
        value = attributes.get("value")
        if not isinstance(value, str) or not value.strip():
            fail("markdown value is empty")
    validations = item.get("validations")
    if item_type == "markdown":
        if validations is not None:
            fail("markdown cannot have validations")
    elif validations is not None:
        if not isinstance(validations, dict) or set(validations) - {"required"}:
            fail(f"body[{index}] validations must only contain required")
        elif not isinstance(validations.get("required"), bool):
            fail(f"body[{index}] required must be a boolean")
    if item_type == "dropdown":
        options = attributes.get("options")
        if not isinstance(options, list) or not options:
            fail(f"dropdown {item.get('id')} needs options")
        else:
            if any(not isinstance(option, str) or not option.strip() for option in options):
                fail(f"dropdown {item.get('id')} has an empty or non-string option")
            if len(options) != len(set(options)):
                fail(f"dropdown {item.get('id')} has duplicate options")
        default = attributes.get("default")
        if default is not None:
            if not isinstance(default, int) or not isinstance(options, list) or not (0 <= default < len(options)):
                fail(f"dropdown {item.get('id')} default is not a valid option index")

if len(ids) != len(set(ids)):
    fail(f"duplicate ids: {ids}")

by_id = {}
for item in body:
    if isinstance(item, dict) and item.get("id"):
        by_id[item["id"]] = item

type_section = labels_md.split("## Type", 1)[1].split("## Priority", 1)[0]
type_labels = re.findall(r"^\| ([a-z][a-z0-9-]*) \|", type_section, re.M)
if "action" not in type_labels:
    fail("ISSUE_LABELS.md type table is missing action")
expected_types = [label.upper() for label in type_labels if label != "action"]
got_types = (by_id.get("action-type") or {}).get("attributes", {}).get("options")
if got_types != expected_types:
    fail(f"Event type options {got_types} != ISSUE_LABELS types {expected_types}")

got_prios = (by_id.get("priority") or {}).get("attributes", {}).get("options")
if got_prios != ["P0", "P1", "P2", "WATCH"]:
    fail(f"Priority options must be P0, P1, P2, WATCH, got {got_prios}")

for item in body:
    if not isinstance(item, dict) or item.get("type") == "markdown":
        continue
    if "validations" not in item or "required" not in item["validations"]:
        fail(f"{item.get('id')} must declare validations.required")

required_ids = {
    "action-type", "priority", "effort", "decision", "why", "evidence",
    "source", "understanding", "summary", "next-action", "done", "progress",
}
optional_ids = {"result", "follow-up"}
if set(ids) != required_ids | optional_ids:
    fail(f"unexpected field ids: {ids}")
for item_id in required_ids:
    if by_id[item_id]["validations"]["required"] is not True:
        fail(f"{item_id} must be required")
for item_id in optional_ids:
    if by_id[item_id]["validations"]["required"] is not False:
        fail(f"{item_id} must be optional")

status_line = by_id["progress"]["attributes"].get("description", "")
for status in ("TODO", "DOING", "BLOCKED", "DONE", "WATCHING", "DROPPED"):
    if status not in status_line or status not in labels_md:
        fail(f"status {status} must stay in the form and ISSUE_LABELS.md")

headings = re.findall(r"^### (.+)$", skeleton, re.M)
if headings != field_labels:
    fail(f"skeleton headings {headings} != form labels {field_labels}")

def first_value(heading):
    lines = skeleton.splitlines()
    for i, line in enumerate(lines):
        if line == f"### {heading}":
            for follow in lines[i + 1:]:
                if follow.startswith("### "):
                    return ""
                if follow.strip():
                    return follow.strip()
    return ""

if first_value("Event type") not in got_types:
    fail("skeleton Event type value is not a dropdown option")
if first_value("Priority") not in got_prios:
    fail("skeleton Priority value is not a dropdown option")
effort_options = by_id["effort"]["attributes"]["options"]
if first_value("Effort") not in effort_options:
    fail("skeleton Effort value is not a dropdown option")

if "1 type + 1 priority + 0–3 topic labels" not in labels_md:
    fail("labeling rule must stay 1 type + 1 priority + 0–3 topic labels")
if "WATCH** is a priority-level option meaning no p-label" not in labels_md:
    fail("ISSUE_LABELS.md must document WATCH as a priority-level option with no p-label")

order = "decision → trust / evidence → understand → act → learn"
if order not in readme:
    fail("README issue workflow must use the new field order")
if "docs/issue-body-skeleton.md" not in readme:
    fail("README must link the issue body skeleton")
if ".github/ISSUE_LABELS.md" not in readme:
    fail("README must link .github/ISSUE_LABELS.md")
if "docs/last30days-intake.md" not in readme:
    fail("README must link docs/last30days-intake.md")
if not Path("docs/last30days-intake.md").is_file():
    fail("docs/last30days-intake.md is missing")
if "wiki/index.md" not in readme:
    fail("README must link wiki/index.md")
for needed in ("scripts/build-wiki.py", "scripts/check-wiki.py", ".github/workflows/build-wiki.yml"):
    if not Path(needed).is_file():
        fail(f"{needed} is missing")

raw_workflow = workflow_path.read_text()
if "types: [opened, edited, reopened]" not in raw_workflow:
    fail("workflow must run on opened, edited, and reopened")
run = workflow["jobs"]["label"]["steps"][0]["run"]
for needle in ("### $1", "Unrecognized event type", "Unrecognized priority", "WATCH", "watch"):
    if needle not in run:
        fail(f"workflow script missing {needle}")
Path("/tmp/label-actions-run.sh").write_text(run if run.endswith("\n") else run + "\n")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("schema: issue form, skeleton headings, and label docs match")
PY

shellcheck -s bash /tmp/label-actions-run.sh
echo "shellcheck: label-actions.yml bash is clean"

run_case() {
  local name="$1"
  local body="$2"
  local current="$3"
  local expect_add="$4"
  local expect_remove="$5"
  local expect_final="$6"
  local expect_log="$7"

  local dir
  dir="$(mktemp -d)"
  printf '%s\n' "$body" > "$dir/body.md"
  printf '%s\n' "$current" > "$dir/labels.txt"
  : > "$dir/edit.log"

  local stdout stderr
  stdout="$dir/stdout.txt"
  stderr="$dir/stderr.txt"
  if ! FIXTURE_BODY_FILE="$dir/body.md" \
    FIXTURE_LABELS_FILE="$dir/labels.txt" \
    EDIT_FILE="$dir/edit.log" \
    GH_TOKEN=test \
    GH_REPO=geekjourneyx/agendum \
    ISSUE_NUMBER=7 \
    bash -c '
      set -euo pipefail
      gh() {
        if [[ "$1" == issue && "$2" == view ]]; then
          local prev="" json="" arg
          for arg in "$@"; do
            if [[ "$prev" == --json ]]; then
              json="$arg"
            fi
            prev="$arg"
          done
          if [[ "$json" == body ]]; then
            cat "$FIXTURE_BODY_FILE"
            return 0
          fi
          if [[ "$json" == labels ]]; then
            cat "$FIXTURE_LABELS_FILE"
            return 0
          fi
          echo "unexpected gh issue view --json $json" >&2
          return 1
        fi
        if [[ "$1" == issue && "$2" == edit ]]; then
          printf "%s\n" "$*" >> "$EDIT_FILE"
          return 0
        fi
        echo "unexpected gh call: $*" >&2
        return 1
      }
      # shellcheck disable=SC1091
      source /tmp/label-actions-run.sh
    ' >"$stdout" 2>"$stderr"; then
    echo "FAIL $name: workflow exited non-zero" >&2
    cat "$stderr" "$stdout" >&2
    exit 1
  fi
  if [[ -s "$stderr" ]]; then
    echo "FAIL $name: unexpected stderr" >&2
    cat "$stderr" >&2
    exit 1
  fi

  local edit
  edit="$(cat "$dir/edit.log")"
  local add="" remove=""
  if [[ -n "$edit" ]]; then
    if [[ "$(wc -l < "$dir/edit.log" | tr -d ' ')" -ne 1 ]]; then
      echo "FAIL $name: expected one gh issue edit, got:" >&2
      cat "$dir/edit.log" >&2
      exit 1
    fi
    add="$(printf '%s\n' "$edit" | sed -n 's/.*--add-label \([^ ]*\).*/\1/p')"
    remove="$(printf '%s\n' "$edit" | sed -n 's/.*--remove-label \([^ ]*\).*/\1/p')"
  fi
  if [[ "$add" != "$expect_add" || "$remove" != "$expect_remove" ]]; then
    echo "FAIL $name: add='$add' remove='$remove'" >&2
    echo " expected add='$expect_add' remove='$expect_remove'" >&2
    echo " edit: $edit" >&2
    exit 1
  fi

  local -a final=()
  local label
  while IFS= read -r label; do
    [[ -n "$label" ]] && final+=("$label")
  done < "$dir/labels.txt"
  local -a kept=()
  local drop item
  for label in "${final[@]}"; do
    drop=0
    if [[ -n "$remove" ]]; then
      IFS=',' read -r -a removed_items <<< "$remove"
      for item in "${removed_items[@]}"; do
        if [[ "$label" == "$item" ]]; then
          drop=1
        fi
      done
    fi
    if [[ "$drop" -eq 0 ]]; then
      kept+=("$label")
    fi
  done
  if [[ -n "$add" ]]; then
    IFS=',' read -r -a added_items <<< "$add"
    for item in "${added_items[@]}"; do
      local seen=0
      for label in "${kept[@]-}"; do
        if [[ "$label" == "$item" ]]; then
          seen=1
        fi
      done
      if [[ "$seen" -eq 0 ]]; then
        kept+=("$item")
      fi
    done
  fi
  local actual
  actual="$(printf '%s\n' "${kept[@]-}" | sed '/^$/d' | sort | paste -sd, -)"
  local expected_sorted
  expected_sorted="$(printf '%s\n' "$expect_final" | tr ',' '\n' | sed '/^$/d' | sort | paste -sd, -)"
  if [[ "$actual" != "$expected_sorted" ]]; then
    echo "FAIL $name: final labels '$actual' != '$expected_sorted'" >&2
    exit 1
  fi

  if [[ -n "$expect_log" ]]; then
    local line
    while IFS= read -r line; do
      if ! grep -Fqx "$line" "$stdout"; then
        echo "FAIL $name: missing log line: $line" >&2
        echo "stdout:" >&2
        cat "$stdout" >&2
        exit 1
      fi
    done <<< "$expect_log"
  elif [[ -s "$stdout" ]]; then
    echo "FAIL $name: unexpected log" >&2
    cat "$stdout" >&2
    exit 1
  fi

  echo "PASS $name -> $expected_sorted"
  rm -rf "$dir"
}

run_case \
  "WATCH type ignores BUILD READ P0 in the body" \
  "$(cat <<'EOF'
### Event type

WATCH
BUILD READ P0

### Priority

WATCH

### Core judgment

BUILD READ P0 appears in the prose, and so does README.
EOF
)" \
  "$(printf '%s\n' read build p0)" \
  "watch" \
  "read,build,p0" \
  "watch" \
  ""

run_case \
  "READ type keeps read when the body contains README" \
  "$(cat <<'EOF'
### Event type

READ
README

### Priority

P2

### Core judgment

See the README before any BUILD.
EOF
)" \
  "$(printf '%s\n' build p0 watch)" \
  "read,p2" \
  "build,watch,p0" \
  "read,p2" \
  ""

run_case \
  "priority P1 is the first line, not a later P0" \
  "$(cat <<'EOF'
### Event type

RESEARCH

### Priority

P1
P0

### Core judgment

The body also says P0, P2, BUILD, and READ. Priority stays P1.
EOF
)" \
  "$(printf '%s\n' read p0 p2)" \
  "research,p1" \
  "read,p0,p2" \
  "p1,research" \
  ""

run_case \
  "unknown type and priority are logged and skipped" \
  "$(cat <<'EOF'
### Event type

TRANSLATE

### Priority

URGENT

### Core judgment

README mentions BUILD and P0, which must not become labels.
EOF
)" \
  "$(printf '%s\n' read p1)" \
  "" \
  "" \
  "p1,read" \
  "$(printf '%s\n' "Unrecognized event type: 'TRANSLATE', skipping the type label" "Unrecognized priority: 'URGENT', skipping the priority label")"

run_case \
  "WATCH priority on UPDATE keeps watch and drops p-labels" \
  "$(cat <<'EOF'
### Event type

UPDATE

### Priority

WATCH

### Core judgment

Observation only. The word P0 in this sentence is not the priority.
EOF
)" \
  "$(printf '%s\n' watch p0 p1 ai read)" \
  "update,watch" \
  "read,p0,p1" \
  "ai,update,watch" \
  ""

run_case \
  "WATCH type suppresses a P0 priority line" \
  "$(cat <<'EOF'
### Event type

WATCH

### Priority

P0

### Core judgment

Type WATCH never receives a p-label.
EOF
)" \
  "$(printf '%s\n' p0 read)" \
  "watch" \
  "read,p0" \
  "watch" \
  ""

echo "all label cases passed"
