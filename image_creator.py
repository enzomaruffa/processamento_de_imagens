import cv2
import numpy as np
import sys

w = int(sys.argv[2])
h = int(sys.argv[1])

new_image = np.zeros(shape=[h, w, 1], dtype=np.uint8)

print(new_image.shape)

for i in range(h):
    for j in range(w):
        color = 0
        if (i + j) % 2 == 1:
            color = 255
        new_image[i][j] = color

cv2.imwrite("generated.png", new_image)
