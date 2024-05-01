import argparse
import os

from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", help="Directory name", nargs="+")
parser.add_argument("-f", "--file", help="File name")
args = parser.parse_args()

path_file = args.file
if args.dir:
    path_dir = ""
    for name in args.dir:
        path_dir += os.path.join(name + os.sep)
    path_file = os.path.join(path_dir, args.file)
    os.makedirs(path_dir, exist_ok=True)

with open(path_file, "a") as file:
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    count = 1
    while True:
        line = input("Enter content line:")
        if line.lower() == "stop":
            break
        file.write(f"{count} {line}" + "\n")
        count += 1
