import numpy as np
import re

data = open(r"input\01.txt", 'r')
lines = [line.strip() for line in data]
inputdata = np.asarray(lines)

############################## PART 1 ##############################

nr_of_elves = np.argwhere(inputdata == '').shape[0] + 1
elves_inventory = np.zeros(nr_of_elves, dtype=np.int32)

index = 0
for calorie in inputdata:
    if calorie == '':
        index += 1
        continue
    elves_inventory[index] += int(calorie)

print(f"the elf carrying the most is carrying {np.max(elves_inventory)}")

