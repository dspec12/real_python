#!/usr/bin/env python3

import os

with open("poem.txt", "r") as f:
    for line in f:
        print(line.readline)