import os
import hashlib


def print_hi(name):
    try:
        if os.path.isdir(name):
            for paths, dirs, files in os.walk(name):
                for file in files:
                    with open(os.path.join(paths, file), "rb") as f:
                        print(os.path.join(paths, file), "\n", os.stat(os.path.join(paths, file)), "\n",
                              "sha256:", hashlib.sha256(f.read()).hexdigest(), "\n", "md5:",
                              hashlib.md5(f.read()).hexdigest(), "\n")
        elif os.path.isfile(name):
            with open(name, "rb") as f:
                print(os.path.abspath(name), "\n", os.stat(os.path.abspath(name)), "\n",
                      "sha256:", hashlib.sha256(f.read()).hexdigest(), "\n", "md5:",
                      hashlib.md5(f.read()).hexdigest(), "\n")
    except Exception as err:
        print(err)
        pass


filepath = input("input file/Filepath: ")
print_hi(filepath)
