import numpy as np
import dill
from pathlib import Path


def printerbeepboop(pos: list, previous_pos: int, space: int, current_dir):
    dir_str =  get_formatted_string(pos, space, "\U0001F4C2 " + current_dir.name)
    global output
    output += dir_str + "\n"
    pos.append(previous_pos)
    for dir in current_dir.dirs:
        printerbeepboop(pos, space, space+17, dir)
    for file in current_dir.files:
        pos.append(space)
        file_str = get_formatted_string(pos, space+15, "\U0001F4D7 "+ file.name)
        output += file_str + "\n"
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
        string[i] = "|"
    return ''.join(string)

if __name__ == "__main__":
    output = ""
    try:
        data = open(r"visuals\07_directory_printing\root_data.pkl", "rb") # run 07.py first to create pickle file
    except:
        print("file does not exist, you probably need to run 07.py first")
        raise
    root = dill.load(data)
    printerbeepboop([], 0, 0, root)
    path = Path(__file__).parent
    file = open(path / 'printed_directory.txt', 'w', encoding='utf-8')
    file.write(output)
    file.close()