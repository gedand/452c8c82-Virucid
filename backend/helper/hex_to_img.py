import binascii
import io
import os
import struct
import sys


import numpy as np
from PIL import Image, ImageDraw


def hex_to_int(h):
    # return int(struct.unpack("H", h)[0])
    try:
        return int(h, 16)
    except:
        # print(h, end=" ")
        return 0
    # return int(h, 16)


def caff_to_jpeg(filename):
    try:
        # data = np.zeros((667, 1000, 3), dtype=np.uint8)
        # k = 0
        # print(filename)
        # file = open(filename, 'rb')
        # a = int(file.readline())
        # b = int(file.readline())
        # # ciff_line = file.readline()
        # ciff_line = binascii.hexlify(file.readline())
        # print(ciff_line[0:20])
        # print(a, 'hi1', b, len(ciff_line))
        #
        # for i in range(0, b):
        #     for j in range(0, a):
        #         data[i, j] = [(hex_to_int(ciff_line[k] + ciff_line[k + 1])),
        #                       (hex_to_int(ciff_line[k + 2] + ciff_line[k + 3])),
        #                       (hex_to_int(ciff_line[k + 4] + ciff_line[k + 5]))]
        #         k = k + 6
        #
        # img = Image.fromarray(data)  # Create a PIL image
        # img.show()
        # img.save("your_file.jpeg")

        return filename[:-3] + 'jpg'
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, exc_obj, fname, exc_tb.tb_lineno)
