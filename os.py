# pylint: disable = E1101

import os

file = open("file2.txt", "wb")
file.close()

os.rename("file2.txt", "file.txt")
os.remove("file.txt")
os.mkdir("folder")
os.rmdir("folder")

