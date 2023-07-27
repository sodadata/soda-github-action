import json
import os
import uuid
import sys

namespace = uuid.NAMESPACE_URL

data = {
    "repositoryName": os.getenv("GITHUB_REPOSITORY"),
    "branchName": os.getenv("BRANCH_NAME"),
    "authorName": os.getenv("GITHUB_ACTOR"),
    "prTitle": os.getenv("PR_TITLE"),
    "prNumber": os.getenv("PR_NUMBER"),
    "prUrl": os.getenv("PR_URL"),
}

# Generate a unique ID for this PR across whole Github
if (
    data["repositoryName"] is None
    or data["branchName"] is None
    or data["prNumber"] is None
):
    sys.exit(1)

data["prIdentifier"] = str(
    uuid.uuid5(
        namespace, data["repositoryName"] + data["branchName"] + data["prNumber"]
    )
)

with open("soda_scan_ci_info.json", "w") as f:
    json.dump(data, f)
