# Flower

A small collection of Python scripts for drawing colorful designs with the
standard-library Turtle graphics module, plus an unfinished Streamlit symptom
checker.

## Features

- `FLOWER.py` draws a multicolored flower pattern.
- `syptom recognizer.py` draws a heart outline with colorful decorative rays.
- `HEART.py` contains an unfinished Streamlit symptom-checker prototype.

The two drawing scripts use Python's Turtle graphics, which opens a desktop
graphics window. The symptom checker is not currently runnable as-is: its first
line is a shell installation command rather than Python code, and it calls
`load_symptom_data()` without defining that function or providing symptom data.
No script in this project provides medical advice or a diagnosis.

## Technologies

- Python 3
- `turtle`, `colorsys`, `math`, and `random` (Python standard library)
- Streamlit and NLTK are referenced by the unfinished symptom-checker prototype

## Setup

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Make sure the Python installation includes Tcl/Tk so the Turtle graphics
   window can open.
3. No third-party packages are needed for the drawing scripts.

To install the packages referenced by the symptom-checker prototype, use a
terminal:

```bash
python -m pip install streamlit nltk
```

The prototype still needs its invalid first line corrected and the
`load_symptom_data()` function and symptom data implemented before it can run.

## Run

From the project folder, run either drawing:

```bash
python FLOWER.py
python "syptom recognizer.py"
```

Each command opens a Turtle graphics window. Close the window to end the
program.

Once the symptom-checker prototype is completed, it can be launched with
Streamlit using:

```bash
streamlit run HEART.py
```

That command will not work with the current `HEART.py` until the missing
implementation and invalid first line described above are addressed.
