# Soda GitHub Action
[![GitHub Super-Linter](https://github.com/sodadata/soda-github-action/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![.github/workflows/tests.yaml](https://github.com/sodadata/soda-github-action/actions/workflows/tests.yaml/badge.svg)](https://github.com/sodadata/soda-github-action/actions/workflows/tests.yaml)

**Soda** enables Data Engineers to test data for quality where and when they need to. It works by taking the data quality checks that you prepare and using them to run a scan of datasets in a data source.
A scan is a CLI command which instructs Soda to prepare optimized SQL queries that execute data quality checks on your data source to find invalid, missing, or unexpected data. When checks fail, they surface bad-quality data and present check results that help you investigate and address quality issues.

Add the **GitHub Action for Soda** to your GitHub Workflow to automatically execute scans for data quality during development.

In a repository in which are adding a transformation or making changes to a dbt model, for example, you can add the Soda GitHub Action to your workflow so that with each new PR, or commit to an existing PR, it executes a Soda scan for data quality and presents the results of the scan in a comment in the pull request, and in a report in Soda Cloud.

Where the scan results indicate an issue with data quality, Soda notifies you both in the PR comment, and by email so that you can investigate and address any issues before merging the PR into production.

Refer to [Soda documentation](https://docs.soda.io/soda/quick-start-dev.html) for an example use case.

## Use the Soda GitHub Action

Add the action to your GitHub Workflow, as in the following example in the `Perform Soda Scan` step.

```yaml
name: Scan for data quality

on: pull_request
jobs:
  soda_scan:
    runs-on: ubuntu-latest
    name: Run Soda Scan
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Perform Soda Scan
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
Refer to [testing files](https://github.com/sodadata/soda-github-action/tree/main/testing) and the [test workflow](https://github.com/sodadata/soda-github-action/blob/main/.github/workflows/tests.yaml) for more context for the example.


### Action inputs
| Name | Description | Required | Default |
| --- | --- | :---: | :---: |
| `soda_library_version` | Version of the Soda Library that runs the scan. Supply a specific version, such as `v1.0.4`, or `latest`. <br /> See [soda-library](https://hub.docker.com/r/sodadata/soda-library/tags) docker images for possible versions. Compatible with Soda Library 1.0.4 and higher. | ✅ | - |
| `data_source` | Name of data source on which to perform the scan. | ✅ | - |
| `configuration` | File path to configuration YAML file. See [Soda docs](https://go.soda.io/configure). | ✅ | - |
| `checks` | File path to checks YAML file. See [Soda docs](https://go.soda.io/configure). Compatible with shell filename extensions.<br /> Identify multiple check files, if you wish. For example: `./checks_*.yaml` or `./{check1.yaml,check2.yaml}` | ✅ | - |


### Self-hosted runners

- Windows runners are not supported, including the use of official Windows-based images such as `windows-latest`.
- MacOS runners require installation of Docker because `macos-latest` does not come with Docker pre-installed.

Access [Soda documentation](https://go.soda.io/docs) for more information.