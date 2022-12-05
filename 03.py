import numpy as np
import re

data = open(r"input\03.txt", 'r')
lines = [line.strip() for line in data]
inputdata = np.asarray(lines)

############################## PART 1 ##############################

priority_sum = 0
for line in inputdata:
    compartement_1 = np.asarray([c for c in line[:len(line)//2]])
    compartement_2 = np.asarray([c for c in line[len(line)//2:]])

    item = np.intersect1d(compartement_1, compartement_2)[0]
    priority_sum += ord(item)-96 if item.islower() else ord(item)-38
    
print(f"the sum of the priorities is {priority_sum}")

############################## PART 1 ##############################