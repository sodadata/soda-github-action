import json
import os
import uuid
import sys

namespace = uuid.NAMESPACE_URL

data = {
    "repository": os.getenv("GITHUB_REPOSITORY"),
    "branch": os.getenv("BRANCH_NAME"),
    "author": os.getenv("GITHUB_ACTOR"),
    "prTitle": os.getenv("PR_TITLE"),
    "prNumber": os.getenv("PR_NUMBER"),
    "prUrl": os.getenv("PR_URL"),
}

# Generate a unique ID for this PR across whole Github
if (
    data["repository"] is None
    or data["branch"] is None
    or data["prNumber"] is None
):
    sys.exit(1)

data["prIdentifier"] = str(
    uuid.uuid5(
        namespace, data["repository"] + data["branch"] + data["prNumber"]
    )
)

with open("soda_scan_ci_info.json", "w") as f:
    json.dump(data, f)
