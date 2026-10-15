# scheduled-shutdown-tool

A tiny Windows desktop tool (Python + Tkinter) that shuts down the PC after a
user-selected countdown, with a fullscreen warning screen so you have time to
save your work.

## Features

- Preset countdown durations: 1 / 3 / 5 / 10 / 20 / 30 minutes (5 minutes default)
- One-click start from the main window
- Fullscreen countdown screen with remaining time and a reminder message
- Background color alternates while time is running out
- Two buttons on the warning screen: shut down immediately, or cancel the pending shutdown
- Uses the built-in Windows system shutdown utility to power off or abort

## Requirements

- Windows (the tool relies on the built-in system shutdown command)
- Python 3 with Tkinter (bundled with the standard Python installer)
- No third-party packages required

## Usage

```bash
python main.py
```

1. Pick a countdown duration in the dropdown.
2. Click the run button. A fullscreen warning appears with the remaining time.
3. Wait for the countdown to reach zero, or use the on-screen buttons to cancel
   the pending shutdown or power off immediately.