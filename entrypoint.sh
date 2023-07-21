#!/bin/sh

python3 /tmp/action_path/scripts/create_ci_info_json.py

soda scan \
  -d "$1" \
  -c /tmp/workspace/"$2" \
  /tmp/workspace/"$3" \
  -srf soda_scan_results_raw.json \
  --scan-type cicd \
  -cif soda_scan_ci_info.json

exit_status=$?

python3 /tmp/action_path/scripts/reformat_json.py soda_scan_results_raw.json

echo $SODA_SCAN_REFERENCE
echo $SODA_CLOUD_URL

{
  echo "SCAN_RESULTS=$(cat soda_scan_results.json)"
  echo "SCAN_EXIT_CODE=$exit_status"
} >> "$GITHUB_ENV"

exit $exit_status