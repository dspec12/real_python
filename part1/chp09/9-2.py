#!/usr/bin/env python3

import os
import glob
import fnmatch

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
all_pngs = glob.glob(os.path.join(images_dir, "**/*.png"), recursive=True)
for png in all_pngs:
    os.rename(png, png[:-3] + "jpg")

'''
4.)
'''
print()
print("4.)")
for current_dir, subdirs, files in os.walk(images_dir):
    for file in files:
        jpgs = os.path.join(images_dir, file)
        if fnmatch.fnmatch(jpgs, "*.jpg") == True:
            print(os.path.exists(jpgs))