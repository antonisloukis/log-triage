# log-triage

A minimal Python CLI for quickly summarizing application log severity.

Built as my personal completion of the DEV Community GitHub Copilot CLI challenge prompt.

## What it does

`log-triage` scans a log file and counts:

- `INFO`
- `WARNING`
- `ERROR`

If at least one `ERROR` line is found, the CLI exits with code `1`.

If no errors are found, it exits with code `0`.

## Usage

Run:

```bash
python3 log_triage.py sample.log
```

Example output:

```text
Log summary for: sample.log
ERROR: 1
WARNING: 2
INFO: 4
```

Check the exit code:

```bash
echo $?
```

With errors present:

```text
1
```

With a healthy log file:

```text
0
```

## Example files

The repository includes:

- `sample.log` — contains INFO, WARNING, and ERROR entries
- `healthy.log` — contains no ERROR entries

## Why this is useful

The exit-code behavior makes the tool useful for simple DevOps and CI/CD workflows.

For example, a pipeline could run the checker after a test or deployment step and fail automatically if error-level log entries are detected.

## GitHub Copilot CLI

GitHub Copilot CLI was used to help:

- generate the initial CLI
- create realistic sample log data
- test the tool
- verify exit-code behavior
- review the implementation

The project intentionally uses only the Python standard library and remains small and beginner-friendly.

## Challenge

Inspired by the DEV Community **GitHub Copilot CLI Challenge**.
