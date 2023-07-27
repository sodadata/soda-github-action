# soda-github-action
[![GitHub Super-Linter](https://github.com/sodadata/soda-github-action/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![.github/workflows/tests.yaml](https://github.com/sodadata/soda-github-action/actions/workflows/tests.yaml/badge.svg)](https://github.com/sodadata/soda-github-action/actions/workflows/tests.yaml)

## Example usage

```yaml
- name: Soda scan
  uses: sodadata/soda-github-action@v1
  env:
    SODA_CLOUD_API_KEY: ${{ secrets.SODA_CLOUD_API_KEY }}
    SODA_CLOUD_API_SECRET: ${{ secrets.SODA_CLOUD_API_SECRET }}
    SNOWFLAKE_USERNAME: ${{ secrets.SNOWFLAKE_USERNAME }}
    SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
  with:
    soda_library_version: v1.0.4
    data_source: snowflake
    configuration: ./configuration.yaml
    checks: ./checks.yaml
```
Also refer to [testing files](https://github.com/sodadata/soda-github-action/tree/main/testing) and the [test workflow](https://github.com/sodadata/soda-github-action/blob/main/.github/workflows/tests.yaml) for complete example of usage.


### Action inputs
| Name | Description | Required | Default |
| --- | --- | --- | --- |
| `soda_library_version` | Version of the Soda Library used to run the scan. Either specific version like `v1.0.4` or `latest`. See [soda-library](https://hub.docker.com/r/sodadata/soda-library/tags) docker images for possible versions. Versions lower than 1.0.4 are not supported. | ✅ | - |
| `data_source` | Data Source name to be used for the scan | ✅ | - |
| `configuration` | Configuration file path. See [docs](https://docs.soda.io/soda-core/configuration.html) | ✅ | - |
| `checks` | Checks file path. See [docs](https://docs.soda.io/soda-core/scan-core.html#anatomy-of-a-scan-command). Allows for using shell filename extensions. You can match multiple check files, for example: `checks: ./checks_*.yaml` or `checks: ./{check1.yaml,check2.yaml}` | ✅ | - |


### Permissions
When using the action in `pull_request` event, it is required to specify step's permissions as follows:
```yaml
permissions: 
   pull-requests: write 
```
as the action posts a comment with the scan results to the PR.
Note the comment is only created for workflows run by `pull_request` event.

### Self-hosted runners caveats
When running this action on self-hosted runners, there are some additional caveats:

- Windows runners are not supported. This also means using official Windows-based images like `windows-latest` is not allowed.
- Mac runners require Docker to be installed additionally. In other words, `macos-latest` does not come with Docker pre-installed.