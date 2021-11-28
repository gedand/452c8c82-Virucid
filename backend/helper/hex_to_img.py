import io

import numpy as np
from PIL import Image


def hex_to_int(h):
    return int(h, 16)


def caff_to_jpeg(filename):
    k = 0

    f = io.open(filename, "rb")
    rl = f.read()
    a = b = y = 0
    for i in range(len(rl)):
        if rl[i] == 10 and y != 0:
            b = rl[y + 1:i]
            y = i + 1
            break
        if rl[i] == 10 and y == 0:
            a = rl[:i]
            y = i
    a = int(a)
    b = int(b)
    hex_res = (rl[y:]).hex()
    data = np.zeros((b, a, 3), dtype=np.uint8)
    for i in range(0, b):
        for j in range(0, a):
            data[i, j] = [(hex_to_int(hex_res[k] + hex_res[k + 1])), (hex_to_int(hex_res[k + 2] + hex_res[k + 3])),
                          (hex_to_int(hex_res[k + 4] + hex_res[k + 5]))]
            k = k + 6

    img = Image.fromarray(data)  # Create a PIL image
    # img.show()
    name = "your_file.jpeg"
    img.save(name)
    return name
