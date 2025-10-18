#!/usr/bin/env python3
import os, re, json, datetime, yaml, sys, subprocess

ROOT = os.path.dirname(__file__)
REPO = os.path.abspath(os.path.join(ROOT, ".."))
os.chdir(REPO)  # ensure git diff runs from repo root

dry_run = "--dry-run" in sys.argv or "-n" in sys.argv

# Load repo version (e.g., 0.1)
with open(os.path.join(REPO, "version.json")) as f:
    repo_ver = json.load(f)["repoVersion"].strip()
prefix_match = re.match(r"^\d+\.\d+", repo_ver)
if not prefix_match:
    raise ValueError(f"Invalid repoVersion format: {repo_ver}")
prefix = prefix_match.group()


def get_changed_docs():
    """Detect Markdown files with material body edits since last commit."""
    try:
        diff = subprocess.check_output(
            ["git", "diff", "--unified=0", "HEAD~1", "HEAD", "--", "*.md"]
        ).decode()
    except subprocess.CalledProcessError:
        return []

    changed = []
    current = None
    for line in diff.splitlines():
        if line.startswith("diff --git"):
            parts = line.split(" b/")
            current = parts[1] if len(parts) == 2 else None
        elif line.startswith("+") or line.startswith("-"):
            if re.match(r"^[-+](version:|lastReviewed:|---)", line.strip()):
                continue
            if current and current not in changed:
                changed.append(current)
    return changed


changed_files = get_changed_docs()
today = datetime.date.today().isoformat()
updated = []

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

        m = re.match(r"---\n(.*?)\n---", text, re.S)
        if not m:
            continue
        front = yaml.safe_load(m.group(1)) or {}
        ver = str(front.get("version", "")).strip()

        if rel in changed_files:
            parts = re.match(r"^(\d+)\.(\d+)\.(\d+)$", ver)
            if parts and ver.startswith(prefix):
                major, minor, patch = map(int, parts.groups())
                new_ver = f"{major}.{minor}.{patch + 1}"
            else:
                new_ver = f"{prefix}.0"
        else:
            new_ver = ver if re.match(r"^\d+\.\d+\.\d+$", ver) and ver.startswith(prefix) else f"{prefix}.0"

        front["version"] = new_ver
        front["lastReviewed"] = today
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
for rel, old, new, changed in updated:
    if old == new:
        continue
    mark = "★" if changed else "•"
    print(f" {mark} {rel}: {old or 'MISSING'} → {new}")

print("\n✅ Version bump complete.")
