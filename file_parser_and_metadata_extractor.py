import platform
import os
import scandir

if platform.system() == 'Windows':
    seperator = "/"
else:
    seperator = "\\"

directory = input("Input Directory: ")
media_type = input("Input media to parse: ")
image_list = []
user_media_interest = ["multimedia", "document", "databases", "program", "network", "binary"]
for media in user_media_interest:
    if media in media_type:
        for line in open("multimedia.txt", "r"):
            image_list.append(line.strip().split("|"))

for paths, dirs, files in scandir.walk(directory):
    for file in files:
        if os.path.isfile(os.path.join(paths, file)):
            with open(os.path.join(paths, file), "rb") as f:
                header = str(f.read(32))
                for image_array in image_list:
                    if image_array[0] in header:
                        stats = [os.path.join(paths, file), header, os.stat(os.path.join(paths, file)), "\n"]
                        for x in stats:
                            print(x)
