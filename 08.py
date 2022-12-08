import numpy as np

data = open(r'input\08.txt', 'r')
inputdata = np.asarray([[c for c in line.strip()] for line in data])

############################## PART 1 ##############################

visible = np.zeros_like(inputdata, dtype=bool)

for row in range(inputdata.shape[0]):
    for tree in range(inputdata.shape[1]):
        current_tree = inputdata[row][tree]
        if np.all(inputdata[:row, tree] < current_tree) or np.all(inputdata[row+1:, tree] < current_tree) or np.all(inputdata[row, :tree] < current_tree) or np.all(inputdata[row, tree+1:] < current_tree):
            visible[row][tree] = True
            continue

print(f"the number of visible trees is {np.sum(visible)}")