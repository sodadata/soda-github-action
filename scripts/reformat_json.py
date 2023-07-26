import json
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
            "State": "Pass",
            "Number of checks": checksMetadata.get("pass"),
        },
        {
            "State": "Warn",
            "Number of checks": checksMetadata.get("warn"),
        },
        {
            "State": "Fail",
            "Number of checks": checksMetadata.get("fail"),
        },
    ]

    with open("soda_scan_results.json", "w") as f:
        json.dump(table_data, f)

    if data.get("cloudUrl") is None or data.get("scanReference") is None:
        sys.exit(1)

    # Construct the URL to the scan results and return it
    print(data.get("cloudUrl") + "/scans/" + data.get("scanReference"))

    sys.exit(0)

except FileNotFoundError:
    sys.exit(1)
except json.JSONDecodeError:
    sys.exit(1)
