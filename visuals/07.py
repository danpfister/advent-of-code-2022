import numpy as np
import re
import time

class file():
    def __init__(self, size: int, name: str) -> None:
        self.size = size
        self.name = name
    
    def __repr__(self) -> str:
        return self.name

class dir():
    def __init__(self, head: dir, name: str) -> None:
        self.name = name
        self.head = head
        self.files = []
        self.dirs = []
        self.size = 0
    
    def __repr__(self) -> str:
        return self.name
    
    def add_file(self, file: file):
        self.files.append(file)
        
    def add_dir(self, dir: dir):
        self.dirs.append(dir)

def parse_input(inputdata):
    root = dir(None, '/')
    current_dir = root
        
    for line in inputdata[1:]:
        if line[0] == '$':
            if line == '$ ls':
                continue
            elif line == '$ cd ..':
                current_dir = current_dir.head
                continue
            else:
                match = re.match(re.compile(r'\$\scd\s(\w+)'), line)
                next_dir = match.group(1)
                for directory in current_dir.dirs:
                    if repr(directory) == next_dir:
                        current_dir = directory
                        break
                continue
            
        match = re.match(re.compile(r'(?:(dir\s(\w+))|((\d+)\s(.+)))'), line)
        '''group 1 is dir, group 3 is file
        group 2 is dir name, group 4 is file size, group 5 is file name'''
        if match.group(1) is not None:
            new_dir = dir(current_dir, match.group(2))
            current_dir.add_dir(new_dir)
        else:
            new_file = file(int(match.group(4)), match.group(5))
            current_dir.add_file(new_file)
    
    return root

def printerbeepboop(pos: list, previous_pos: int, space: int, current_dir: dir):
    dir_str =  get_formatted_string(pos, space, current_dir.name)
    print(dir_str)
    time.sleep(0.05)
    pos.append(previous_pos)
    for dir in current_dir.dirs:
        printerbeepboop(pos, space, space+15, dir)
    for file in current_dir.files:
        pos.append(space)
        file_str = get_formatted_string(pos, space+15, file.name)
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
    data = open(r".\input\07.txt", 'r')
    inputdata = np.asarray([line.strip() for line in data])
    root = parse_input(inputdata)
    printerbeepboop([], 0, 0, root)