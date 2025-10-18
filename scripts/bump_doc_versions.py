#!/usr/bin/env python3
import os, re, json, datetime, yaml, subprocess, sys

# CI-only bump: diff PR branch vs base (origin/main), bump changed .md files, no prompts.

ROOT = os.path.dirname(__file__)
REPO = os.path.abspath(os.path.join(ROOT, ".."))
os.chdir(REPO)

def sh(args, check=False):
    return subprocess.run(args, cwd=REPO, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=check)

def merge_base():
    # Resolve base commit against origin/main; fallback to HEAD~1 if needed
    mb = sh(["git", "merge-base", "HEAD", "origin/main"])
    if mb.returncode == 0 and mb.stdout.strip():
        return mb.stdout.strip()
    hb = sh(["git", "rev-parse", "HEAD~1"])
    return hb.stdout.strip() if hb.returncode == 0 else "HEAD"

# load repo version prefix (e.g., "0.1")
with open(os.path.join(REPO, "version.json"), encoding="utf-8") as f:
    repo_ver = json.load(f)["repoVersion"].strip()
m = re.match(r"^\d+\.\d+", repo_ver)
if not m:
    print("Invalid repoVersion in version.json"); sys.exit(2)
prefix = m.group()
today = datetime.date.today().isoformat()

base = merge_base()

# list changed markdown files between base..HEAD (recursive pathspec)
diff = sh(["git", "diff", "--name-only", f"{base}...HEAD", "--", ":(glob)**/*.md"])
paths = [p.strip() for p in diff.stdout.splitlines() if p.strip()]
if not paths:
    print("ℹ️ No markdown changes vs base.")
    sys.exit(0)

changed = set(paths)

bumped = []
for rel in sorted(changed):
    path = os.path.join(REPO, rel)
    if not os.path.exists(path):  # deleted/renamed edge cases
        continue
    with open(path, encoding="utf-8") as f:
        text = f.read()

    # require YAML front matter
    m = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        continue

    front = yaml.safe_load(m.group(1)) or {}
    ver = str(front.get("version", "")).strip()

    parts = re.match(r"^(\d+)\.(\d+)\.(\d+)$", ver) if ver else None
    if parts and ver.startswith(prefix):
        a, b, c = map(int, parts.groups())
        new_ver = f"{a}.{b}.{c+1}"
    else:
        new_ver = f"{prefix}.0"

    # update front matter
    front["version"] = new_ver
    front["lastReviewed"] = today

    new_front = yaml.dump(front, sort_keys=False).strip()
    body = re.sub(r"^---\r?\n.*?\r?\n---\r?\n", "", text, flags=re.S)
    new_text = f"---\n{new_front}\n---\n{body}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

    bumped.append((rel, ver or "MISSING", new_ver))

# stage, commit, push are handled by workflow; print summary for logs
if not bumped:
    print("ℹ️ No front-matter docs to bump.")
    sys.exit(0)

print("✅ Bumped versions:")
for rel, old, newv in bumped:
    print(f"★ {rel}: {old} → {newv}")
