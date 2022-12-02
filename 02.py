import numpy as np
import re

data = open(r"input\02.txt", 'r')
lines = [line.strip() for line in data]
inputdata = np.asarray(lines)

############################## PART 1 ##############################

# A, X: rock, B, Y: paper, C, Z: scissors
value = {'A': 1, 'B': 2, 'C': 3}
mapping = {'X': 'A', 'Y': 'B', 'Z': 'C'}
indexing = {'A': 0, 'B': 1, 'C': 2}
outcome = np.array([[3, 0, 6], [6, 3, 0], [0, 6, 3]])

score = 0
for line in inputdata:
    match = re.match(re.compile(r'(\w)\s(\w)'), line)
    opponent_shape = match.group(1)
    your_shape = mapping[match.group(2)]

    score += outcome[indexing[your_shape]][indexing[opponent_shape]] + value[your_shape]

print(f"your final score is {score}")