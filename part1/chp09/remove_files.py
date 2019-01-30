#!/usr/bin/env python3

import os
import fnmatch

target_dir = "/Users/danielspector/Desktop/little pics"

for current_dir, subdirs, files in os.walk(target_dir):
    for file in files:
        full_path_files = os.path.join(current_dir, file)
        if fnmatch.fnmatch(full_path_files, "*.jpg") and os.path.getsize(full_path_files) < 2000:
            print("Removing", full_path_files)
            os.remove(full_path_files)
