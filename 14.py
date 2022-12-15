import numpy as np
import re

def draw_cave(paths):
    cave = np.full((250, 1000), '.') # first index is top to bottom, second index is left to right 
    for path in paths:
        previous_corner = None
        for corner in path:
            if previous_corner is None:
                cave[corner[0], corner[1]] = '#'
                previous_corner = corner
                continue
            if corner[0] == previous_corner[0]: # horizontal
                cave[corner[0], min(previous_corner[1], corner[1]):max(previous_corner[1], corner[1])+1] = '#'
            else: # vertical
                cave[min(previous_corner[0], corner[0]):max(previous_corner[0], corner[0])+1, corner[1]] = '#'
            previous_corner = corner
    
    return cave

def drop_sand(cave) -> bool:
    current_pos = np.array([0, 500])
    while True:
        if current_pos[0] == cave.shape[0]-1: # dropped into abyss
            return False
        if cave[current_pos[0]+1, current_pos[1]] == '.':
            current_pos += [1, 0]
            continue
        elif cave[current_pos[0]+1, current_pos[1]-1] == '.':
            current_pos += [1, -1]
            continue
        elif cave[current_pos[0]+1, current_pos[1]+1] == '.':
            current_pos += [1, 1]
            continue
        else:
            break
    cave[current_pos[0], current_pos[1]] = 'o'
    return True
    
    
if __name__ == "__main__":
    inputfile = open(r".\input\14.txt", 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    paths = [[[int(corner[1]), int(corner[0])] for corner in re.findall(re.compile(r'(\d+),(\d+)(?: -> )*'), path)] for path in inputdata]
    print(paths)

    cave = draw_cave(paths)
    nr_of_sandblocks = 0
    while drop_sand(cave):
        nr_of_sandblocks += 1
        continue
    
    print(nr_of_sandblocks)