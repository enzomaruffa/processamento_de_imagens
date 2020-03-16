import os
import subprocess

file_names = input("File names? ")
file_names = file_names.split()
print(file_names)

sampling_percentages = input("Sampling percentages? ")
sampling_percentages = sampling_percentages.split()
sampling_percentages = list(map(lambda x: float(x), sampling_percentages))
print(sampling_percentages)

modes = input("Modes? ")
modes = modes.split()
modes = list(map(lambda x: int(x), modes))
print(modes)

greyscale_levels = input("Greyscale levels? ")
greyscale_levels = greyscale_levels.split()
greyscale_levels = list(map(lambda x: int(x), greyscale_levels))
print(greyscale_levels)

count = 0

for file_name in file_names:
    for sampling_percentage in sampling_percentages:
        for mode in modes:
            for levels in greyscale_levels:
                call = "python3 lab1.py " + file_name + " " + str(sampling_percentage) + " " + str(mode) + " " + str(levels)
                print("Calling " + call)
                subprocess.call(call, shell=True)
                
                count += 1

print("Finished processing " + str(count) + " images!")