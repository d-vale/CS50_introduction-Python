import os
import sys

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = {".jpg", ".jpeg", ".png"}

    _, input_ext = os.path.splitext(input_file)
    _, output_ext = os.path.splitext(output_file)

    input_ext = input_ext.lower()
    output_ext = output_ext.lower()

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        img = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_path = os.path.join(os.path.dirname(__file__), "shirt.png")
    shirt = Image.open(shirt_path)

    img = ImageOps.fit(img, shirt.size)
    img.paste(shirt, mask=shirt)
    img.save(output_file)


main()
