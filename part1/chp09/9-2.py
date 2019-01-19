#!/usr/bin/env python3

import os
import glob
images_dir = "/Users/danielspector/Desktop/images"

'''
1.)
'''
print("1.)")
print(os.listdir(images_dir))

'''
2.)
'''
print()
print("2.)")
png_files = os.path.join(images_dir, "*.png")
print(glob.glob(png_files))

'''
3.)
'''
print()
print("3.)")
for current_folder, subfolders, file_names in os.walk(images_dir):
    for file_name in file_names:
        print(os.path.join(current_folder, file_name))


print(os.walk(images_dir))