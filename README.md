# Log Analysis Agent

Lightweight Python agent for simple log analytics and counts extraction from application logs.

## Overview

This repository contains a tiny agent that uses an LLM (via Ollama) and a file-read tool to analyze log files. The example entrypoint, `logs_agent.py`, demonstrates counting log-level occurrences (INFO, WARNING, ERROR) from `app.log`.

## Requirements

- Python 3.10+
- See `requirements.txt` for Python dependencies
- (Optional) Ollama running locally if using the `OllamaModel` backend

## Configuration

Edit `logs_agent.py` to configure the LLM backend:

- `host`: Ollama server URL (default in example: `http://localhost:11434`)
- `model_id`: model name to use (example uses `llama3.2`)

No production actions are performed by the agent — it only reads logs and provides suggestions.

## Usage

1. Fork and clone the repo:

```powershell
git clone <repo-url>
```

2. Install dependencies:

```powershell
py -m pip install -r requirements.txt
```

3. Run the agent (example):

```powershell
py .\logs_agent.py
```

The script calls the agent with a prompt asking to detect how many times `INFO`, `WARNING` and `ERROR` occur in `app.log` and returns counts.

## Example

Given the provided `app.log`, the expected output format is a simple count of occurrences, for example:

```
INFO: 26
WARNING: 6
ERROR: 10
```

(Actual counts depend on the log contents and any duplicate lines.)

## Notes

- The project uses a tool-based approach: `file_read` is passed as a tool to the agent so it can read log files.
- The agent is configured with a system prompt that enforces safety: no production changes, concise answers, and a DevOps mindset for root cause analysis.

## Next steps

- Replace or extend `file_read` to support directory scans or filtering by date.
- Add unit tests for parsing and counting logic if you extract that logic into a module.

