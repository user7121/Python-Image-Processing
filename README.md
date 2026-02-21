# Python Image Processing (Rotate, Resize, Blur)

A simple cross-platform Python project that loads an image, rotates it, resizes it, and applies Gaussian blur using Pillow and Matplotlib without saving output files.

## Requirements

* Python 3.8+
* pillow
* matplotlib

Dependencies are listed in `requirements.txt`.

## Project Structure

```
project/
├── main.py
├── requirements.txt
└── image/
    └── input.png
```

## Installation & Setup

### 🪟 Windows

```bat
cd your-project-folder
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

### 🐧 Linux (Linux Mint / Ubuntu)

```bash
sudo apt update
sudo apt install python3-full python3-venv

cd your-project-folder
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## How to Run

Make sure the image exists at:

```
image/input.png
```

Then run:

```bash
python main.py
```

The program will:

* Rotate the image (45°)
* Resize the image (400×400)
* Apply Gaussian blur
* Display results in labeled windows (no files saved)

## Notes

* Works on Windows and Linux
* Uses a virtual environment (recommended)
* Do not upload `.venv/` to GitHub (already ignored in `.gitignore`)
