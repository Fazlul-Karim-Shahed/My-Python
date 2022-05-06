
from msvcrt import kbhit
import os, sys, random

current_folder = os.getcwd()

files = os.listdir(current_folder)
print(files)
print("File name: ", random.choice(files))
print(random.choices(files, weights=[1,1,1,1,1,1,3,1], k=3))