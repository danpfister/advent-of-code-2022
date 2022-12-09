import numpy as np
import re
import time
import dill
import emoji


def printerbeepboop(pos: list, previous_pos: int, space: int, current_dir):
    dir_str =  get_formatted_string(pos, space, "\U0001F4C2 " + current_dir.name)
    print(dir_str)
    time.sleep(0.05)
    pos.append(previous_pos)
    for dir in current_dir.dirs:
        printerbeepboop(pos, space, space+15, dir)
    for file in current_dir.files:
        pos.append(space)
        file_str = get_formatted_string(pos, space+15, "\U0001F4D7 "+ file.name)
        print(file_str)
        time.sleep(0.05)
        pos.pop()
    pos.pop()
    return

def get_formatted_string(pos: list, name_pos: int, name: str):
    if name_pos == 0:
        return name
    name = " " + name
    string = list(f"{name:->{name_pos}}")
    string[:pos[-1]] = pos[-1] * [' ']
    for i in pos:
        string[i] = "'"
    return ''.join(string)

if __name__ == "__main__":
    data = open(r"visuals\07_directory_printing\root_data.pkl", "rb") # run 07.py first to create pickle file
    root = dill.load(data)
    printerbeepboop([], 0, 0, root)