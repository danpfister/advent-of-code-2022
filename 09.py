import numpy as np
import re

inputfile = open(r".\input\09.txt", "r")
inputdata = np.asarray([line.strip() for line in inputfile])

############################## PART 1 ##############################

head_pos = np.zeros(2, dtype=np.int32)
tail_pos = np.zeros(2, dtype=np.int32)
visited_pos = []
head_movement = {"U": [0, 1], "L": [-1, 0], "D": [0, -1], "R": [1, 0]}
for motion in inputdata:
    match = re.match(re.compile(r"(\w) (\d+)"), motion)
    for movement in range(int(match.group(2))):
        head_pos += head_movement[match.group(1)] # update head position
        if abs(max(diff := head_pos - tail_pos, key=abs)) > 1: # check if head and tail touching
            tail_pos[0] += min(diff[0], 1) if diff[0] > 0 else max(diff[0], -1)
            tail_pos[1] += min(diff[1], 1) if diff[1] > 0 else max(diff[1], -1)
        visited_pos.append((tail_pos[0], tail_pos[1]))
print(f"number of unique positions visited by tail: {len(set(visited_pos))}")