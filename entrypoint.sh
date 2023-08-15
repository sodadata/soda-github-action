#!/bin/sh

python3 /tmp/action_path/scripts/create_ci_info_json.py

# shellcheck disable=SC2086
soda scan \
  -d "$1" \
  -c /tmp/workspace/$2 \
  /tmp/workspace/$3 \
  -srf soda_scan_results_raw.json \
  --scan-type cicd \
  -cif soda_scan_ci_info.json

echo "SCAN_EXIT_CODE=$?" >> $GITHUB_ENV
echo "SCAN_CLOUD_LINK=$(python3 /tmp/action_path/scripts/reformat_json.py soda_scan_results_raw.json)" >> $GITHUB_ENV
echo "SCAN_RESULTS=$(cat soda_scan_results.json 2> /dev/null)" >> $GITHUB_ENV

exit 0
