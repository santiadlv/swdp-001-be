import os
import json
from barcode import EAN14
from barcode.writer import SVGWriter


def create_label_image(label_id: int):
    filename = f"{label_id}.svg"

    with open(filename, "wb") as f:
        EAN14(str(label_id), writer=SVGWriter()).write(f)

    with open(filename, "r") as f:
        svg = f.read()
        encoded_svg = json.dumps(svg)
    
    os.remove(filename)
    return encoded_svg
