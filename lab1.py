import cv2
import numpy as np
import math
import sys

MEAN = 0
MEDIAN = 1
MODE = 2

"""O programa deve receber como parâmetros o nome da imagem, o porcentual de amostragem, 
a técnica de amostragem (média, mediana ou moda.) e a quantidade de níveis de 
cinza [2,4,8,16,32,64,128,256] (quantização)"""

# Reading parameters
image_name = sys.argv[1]
sampling_percentage = float(sys.argv[2])
amostrage_technique = int(sys.argv[3])
grey_level_count = int(sys.argv[4])

if sampling_percentage > 1 or sampling_percentage <= 0:
    exit("sampling_percentage must be > 0 and <= 1")

if amostrage_technique not in [0, 1, 2]:
    exit("amostrage_technique must be in [0, 1, 2]")

if grey_level_count > 256 or grey_level_count <= 1 :
    exit("grey_level_count must be <= 256 and > 1 ")

# print("Parsing image", image_name)
# print("with a sampling percentage of", sampling_percentage)
# print("using as technique", amostrage_technique)
# print("and", grey_level_count, "grey levels \n")

def generate_points(minX, xCount, minY, yCount):
    points = []
    for i in range(minX, minX + xCount):
        for j in range(minY, minY + yCount):
            points.append((i, j))
    return points

def get_colors_in(original_image, points):
    colors = []
    for point in points:
        colors.append(original_image[point[1]][point[0]])
    return colors

def get_color_for(colors, mode):
    if mode == MEAN:
        return np.average(colors)
    elif mode == MEDIAN:
        return np.median(colors)
    elif mode == MODE:
        return np.mode(colors)
    return 255

def get_closest_in(value_list, number):
    return min(value_list, key=lambda x:abs(x-number))

def paint(image, color, points):
    for point in points:
        image[point[1]][point[0]] = color


original_image = cv2.imread(image_name, 0)
original_h, original_w = original_image.shape

new_image = np.zeros(shape=[original_h, original_w, 1], dtype=np.uint8)

new_h = math.ceil(original_h * sampling_percentage)
new_w = math.ceil(original_w * sampling_percentage)

greyscale_levels = np.linspace(0, 255, grey_level_count)

width_step = original_w / new_w
height_step = original_h / new_h

previous_w = 0
max_w = 0
current_image_x = 0

while math.ceil(previous_w) < original_w:   
    max_w = previous_w + width_step
    previous_w_floor = math.floor(previous_w)
    total_w_iteration = math.floor(max_w - previous_w_floor)

    previous_h = 0
    max_h = 0
    current_image_y = 0

    while math.ceil(previous_h) < original_h: 
        max_h = previous_h + height_step
        
        previous_h_floor = math.floor(previous_h)
        total_h_iteration = math.floor(max_h - previous_h_floor)
        
        points = generate_points(previous_w_floor, total_w_iteration, previous_h_floor, total_h_iteration)
        colors = get_colors_in(original_image, points)
        color = get_color_for(colors, MEDIAN)
        
        final_color = get_closest_in(greyscale_levels, color)

        paint(new_image, final_color, points)

        previous_h = max_h

    previous_w = max_w

name = image_name.split(".")[0]

output_name = name + "_" + str(math.ceil(sampling_percentage * 100)) + "_" + str(amostrage_technique) + "_" + str(grey_level_count) + "." + image_name.split(".")[1]
cv2.imwrite(output_name, new_image)
