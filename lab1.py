import cv2
from math import floor

MEAN = 0
MEDIAN = 1
MODE = 2

"""O programa deve receber como parâmetros o nome da imagem, o porcentual de amostragem, 
a técnica de amostragem (média, mediana ou moda.) e a quantidade de níveis de 
cinza [2,4,8,16,32,64,128,256] (quantização)"""

# Reading parameters
image_name = "exemplo.png"
sampling_percentage = 0.51
amostrage_technique = MEAN
grey_level_count = 4

original_image = cv2.imread(image_name, 0)
original_h, original_w = original_image.shape

print(original_h, original_w)

new_h = floor(original_h * sampling_percentage)
new_w = floor(original_w * sampling_percentage)

print(new_h, new_w)

cv2.imshow("test", original_image)