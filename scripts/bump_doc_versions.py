#!/usr/bin/env python3
import os, re, json, datetime, yaml, sys, subprocess

ROOT = os.path.dirname(__file__)
REPO = os.path.abspath(os.path.join(ROOT, ".."))

dry_run = "--dry-run" in sys.argv or "-n" in sys.argv

# Load repo version (e.g., 0.1)
with open(os.path.join(REPO, "version.json")) as f:
    repo_ver = json.load(f)["repoVersion"].strip()
prefix_match = re.match(r"^\d+\.\d+", repo_ver)
if not prefix_match:
    raise ValueError(f"Invalid repoVersion format: {repo_ver}")
prefix = prefix_match.group()

# Detect changed files using git (ignore front-matter-only edits)
def get_changed_docs():
    try:
        # diff only body changes — ignore front-matter lines
        diff = subprocess.check_output(
            ["git", "diff", "--unified=0", "HEAD", "--", "*.md"]
        ).decode()
    except subprocess.CalledProcessError:
        return []

    changed = []
    current_file = None
    for line in diff.splitlines():
        if line.startswith("diff --git"):
            parts = line.split(" b/")
            if len(parts) == 2:
                current_file = parts[1]
        elif line.startswith("+") or line.startswith("-"):
            # ignore front-matter edits (version:, lastReviewed:, --- delimiters)
            if re.match(r"^[-+](version:|lastReviewed:|---)", line.strip()):
                continue
            if current_file and current_file not in changed:
                changed.append(current_file)
    return changed

changed_files = get_changed_docs()
today = datetime.date.today().isoformat()
updated, drift_detected = [], False

# Walk entire repo (not just /docs)
for dirpath, _, files in os.walk(REPO):
    if any(skip in dirpath for skip in [".git", "__pycache__", "node_modules"]):
        continue

    for fn in files:
        if not fn.endswith(".md"):
            continue

        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, REPO)

        with open(path, encoding="utf-8") as f:
            text = f.read()

        # Detect YAML front matter
        m = re.match(r"---\n(.*?)\n---", text, re.S)
        if not m:
            continue
        front = yaml.safe_load(m.group(1)) or {}
        ver = str(front.get("version", "")).strip()
        new_ver = ver

        # Handle versioning rules
        if rel in changed_files:
            # material content changed → bump
            parts = re.match(r"^(\d+)\.(\d+)\.(\d+)$", ver)
            prefix_ok = ver.startswith(prefix)
            if parts and prefix_ok:
                major, minor, patch = map(int, parts.groups())
                new_ver = f"{major}.{minor}.{patch + 1}"
            else:
                new_ver = f"{prefix}.0"
                drift_detected = True
        else:
            # no body change → keep version; normalize if invalid
            if not re.match(r"^\d+\.\d+\.\d+$", ver) or not ver.startswith(prefix):
                new_ver = f"{prefix}.0"
                if ver and ver != new_ver:
                    drift_detected = True
            else:
                new_ver = ver

        # always allow lastReviewed edits
        if "lastReviewed" not in front:
            front["lastReviewed"] = today

        front["version"] = new_ver

        new_front = yaml.dump(front, sort_keys=False).strip()
        body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
        new_text = f"---\n{new_front}\n---\n{body}"

        if not dry_run and rel in changed_files:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)

        updated.append((rel, ver, new_ver, rel in changed_files))

# Summary
if not updated:
    print("ℹ️ No markdown files found.")
    sys.exit(0)

print(f"🔍 {'Previewing' if dry_run else 'Updated'} document versions (repo {repo_ver}):")
print(f"   Immutable version prefix: {prefix}.x\n")

for rel, old, new, did_change in updated:
    if old == new:
        continue
    mark = "★" if did_change else "•"
    note = " (drift)" if old and not re.match(r'^\d+\.\d+\.\d+$', old) else ""
    print(f" {mark} {rel}: {old or 'MISSING'} → {new}{note}")

if dry_run:
    if drift_detected:
        print("\n❌ Drift detected — one or more docs contain user-edited or non-semantic version tags.")
        print(f"   Expected immutable prefix: {prefix}.x (from version.json)")
        print("   Please revert or rerun this script to normalize.\n")
        sys.exit(1)
    else:
        print("\n💡 Dry run only — no files modified.")
else:
    print("\n✅ Version bump complete.")
