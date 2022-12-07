import numpy as np
import re

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

def set_dir_sizes(current_dir: dir):
    for dir in current_dir.dirs:
        current_dir.size += set_dir_sizes(dir)
    for file in current_dir.files:
        current_dir.size += file.size
    return current_dir.size

def get_dir_sizes(total_size: int, current_dir: dir):
    for dir in current_dir.dirs:
        total_size = get_dir_sizes(total_size, dir)
    if current_dir.size <= 100000:
        total_size += current_dir.size
        return total_size
    return total_size

def get_smallest_possible_dir(required_space: int, current_best: dir, current_dir: dir):
    for dir in current_dir.dirs:
        current_best = get_smallest_possible_dir(required_space, current_best, dir)
    if current_dir.size >= required_space and current_dir.size <= current_best.size:
        current_best = current_dir
    return current_best
    
            
if __name__ == "__main__":
    data = open(r"input\07.txt", 'r')
    inputdata = np.asarray([line.strip() for line in data])
    root = parse_input(inputdata)
    set_dir_sizes(root)
    ############################## PART 1 ##############################
    print(f"the sum of the directories with size <= 100000 is {get_dir_sizes(0, root)}")
    ############################## PART 2 ##############################
    required_space = root.size - 40000000
    smallest_possible_dir = get_smallest_possible_dir(required_space, root, root)
    print(f"the smallest possible directory is {smallest_possible_dir} with size {smallest_possible_dir.size}")