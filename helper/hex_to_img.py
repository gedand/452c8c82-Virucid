import numpy as np
from PIL import Image

def hex_to_int(h):
    return int(h,16)

data = np.zeros( (667,1000,3), dtype=np.uint8 )
k=0
ciff_line = open('first_ciff.txt','r').readline()
for i in range(0,667):
    for j in range(0,1000):
        data[i,j] = [(hex_to_int(ciff_line[k]+ciff_line[k+1])),(hex_to_int(ciff_line[k+2]+ciff_line[k+3])),(hex_to_int(ciff_line[k+4]+ciff_line[k+5]))]
        k = k+6

img = Image.fromarray(data)       # Create a PIL image
img.show()  
img.save("your_file.jpeg")
     
