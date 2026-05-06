from pathlib import Path
from rembg import remove

SUPPORTED_TYPES = (".png", ".jpg", ".jpeg", ".webp")

input_dir = Path("input")
output_dir = Path("output")

# Create output directory if it doesn't exist
output_dir.mkdir(exist_ok=True)


def process_image(file):
    output_path = output_dir / (file.stem + ".png")

    with open(file, "rb") as i:
        input_data = i.read()

    output_data = remove(input_data)

    with open(output_path, "wb") as o:
        o.write(output_data)

    print(f"Saved: {output_path}")


# iterdir() returns the files, iterating the Path object directly doesn't work
for file in input_dir.iterdir():
    if file.suffix.lower() not in SUPPORTED_TYPES:
        print(f"Skipping: {file.name}")
        continue

    print(f"Processing: {file.name}")
    process_image(file)

    print(f"Done: {file.name}")

print(f"All files finished")

