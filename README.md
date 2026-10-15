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

## License & Attribution / 许可与来源

Original project code authored for this repository is released under the MIT License; see [LICENSE](./LICENSE).

When reusing or redistributing a substantial portion, retain the LICENSE and its copyright notice. The copyright notice includes this original source URL: https://github.com/change979666/scheduled-shutdown-tool. Please keep the source link visible in your redistributed source or project documentation.

This license applies only to original material that the repository maintainer has the right to license. Third-party libraries, vendor code, platform SDKs, trademarks, screenshots, icons, fonts, and other external assets remain subject to their respective licenses and terms. Review those terms before reuse.

**Project status:** personal/archived project, shared as-is. Maintenance, compatibility, and production readiness are not guaranteed.
