import json
import os

data = {
    "repository": os.getenv("GITHUB_REPOSITORY"),
    "branch": os.getenv("GITHUB_REF_NAME"),
    "author": os.getenv("GITHUB_ACTOR"),
    "prTitle": os.getenv("PR_TITLE"),
}

with open("soda_scan_ci_info.json", "w") as f:
    json.dump(data, f)
