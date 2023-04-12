# from tkinter import filedialog as fd

# filename = fd.askopenfilenames()

# for i in filename:
#     i = i
#     print(i)

# print(filename)
import os
song = "Song1"
song = f'{song}.mp3'
real_path = os.path.realpath(song)
print(real_path)