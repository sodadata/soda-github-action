import json
import os
import sys

json_file_name = sys.argv[1]

try:
    with open(json_file_name, "r") as json_file:
        json_content = json_file.read()

    data = json.loads(json_content)
    checksMetadata = data.get("checksMetadata")
    table_data = [
        {
            "State": "Not evaluated",
            "Number of checks": checksMetadata.get("notEvaluated"),
        },
        {
            "State": "Passed",
            "Number of checks": checksMetadata.get("pass"),
        },
        {
            "State": "Warning",
            "Number of checks": checksMetadata.get("warn"),
        },
        {
            "State": "Failed",
            "Number of checks": checksMetadata.get("fail"),
        },
    ]

    with open("soda_scan_results.json", "w") as f:
        json.dump(table_data, f)

    # Construct the URL to the scan results and return it
    print("https://" + data.get("cloudUrl") + "/scans/" + data.get("scanReference"))

    sys.exit(0)

except FileNotFoundError:
    sys.exit(1)
except json.JSONDecodeError:
    sys.exit(1)
