from collections import Counter
import os
import shutil


folder = input("Where to put your files: ")

if os.path.exists(folder):
    print("Great the folder exists")
else:
    print("Womp womp")


files = os.listdir(folder)

print(files)

images = 0
video = 0 
documents = 0
other = 0

os.mkdir("Images")