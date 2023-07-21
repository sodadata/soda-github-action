import json
import os

data = {
    "repository": os.getenv("GITHUB_REPOSITORY"),
    "branch": os.getenv("BRANCH_NAME"),
    "author": os.getenv("GITHUB_ACTOR"),
    "prTitle": os.getenv("PR_TITLE"),
    "prNumber": os.getenv("PR_NUMBER"),
    "prUrl": os.getenv("PR_URL"),
}

with open("soda_scan_ci_info.json", "w") as f:
    json.dump(data, f)
