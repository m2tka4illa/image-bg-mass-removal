# Background Removal

A simple Python script that automatically removes backgrounds from images using [rembg](https://github.com/danielgatis/rembg).

## Requirements

- Python 3.7+
- macOS (for the symlinks/Automator setup)

## Setup

1. Clone the repository
2. Run the setup script to create a virtual environment and install dependencies:

```bash
chmod +x setup.sh
./setup.sh
```

3. Optionally, create Desktop shortcuts to the `input/` and `output/` folders:

```bash
chmod +x make_symlinks.sh
./make_symlinks.sh
```

## Usage

1. Drop images into the `input/` folder (supported formats: `.png`, `.jpg`, `.jpeg`, `.webp`)
2. Run the script:

```bash
venv/bin/python remove_bg.py
```

3. Processed images will appear in the `output/` folder as `.png` files with transparent backgrounds

## Desktop Shortcut (macOS)

To run the script by double-clicking an icon on the Desktop:

1. Open **Automator** → New Document → **Application**
2. Add a **Run Shell Script** action with:

```bash
cd /path/to/background-removal
venv/bin/python remove_bg.py
```

3. Save it to the Desktop
