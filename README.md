# Python

Python is a small Python project containing two Turtle graphics programs. Run
either script to draw a colorful design in a desktop window.

## Overview and features

- `FLOWER.py` draws a flower-like pattern on a black background using changing
  HSV colors.
- `HEART.py` draws a heart outline with colored radial strokes on a black
  background.

Both programs use Python's built-in Turtle graphics. `HEART.py` chooses stroke
colors randomly each time it runs.

## Technologies

- Python 3
- Python standard library: `turtle`, `colorsys`, `math`, and `random`

No third-party Python packages are required.

## Project structure

```text
.
|-- FLOWER.py  # Turtle flower pattern
|-- HEART.py   # Turtle heart with decorative strokes
|-- README.md  # Project documentation
`-- .gitignore # Files excluded from Git
```

## Setup and installation

1. Install Python 3.
2. Ensure your Python installation includes Tcl/Tk, which is required by
   `turtle` to open its graphics window.
3. Clone this repository or open the project folder. No package installation
   step is needed.

## Run

Open a terminal in the project folder and run either script:

```bash
python FLOWER.py
```

```bash
python HEART.py
```

Each script opens a Turtle graphics window. Close the window to finish.

## Current limitations

- The programs require a desktop environment with a working Turtle/Tk graphics
  window; they are not command-line or headless drawing tools.
- The designs and settings are defined directly in the scripts; there are no
  command-line options or configuration interface.
- `HEART.py` uses random colors, so its result can vary between runs.
