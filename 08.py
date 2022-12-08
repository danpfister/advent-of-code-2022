import numpy as np

data = open(r'input\08.txt', 'r')
inputdata = np.asarray([[c for c in line.strip()] for line in data])

############################## PART 1 ##############################

visible = np.zeros_like(inputdata, dtype=bool)

for row in range(inputdata.shape[0]):
    for tree in range(inputdata.shape[1]):
        current_tree = inputdata[row][tree]
        orientations = [inputdata[:row, tree][::-1], inputdata[row, :tree][::-1], inputdata[row+1:, tree], inputdata[row, tree+1:]] # counter clockwise starting from upwards
        for index, orientation in enumerate(orientations):
            if np.all(orientation < current_tree):
                visible[row][tree] = True
                break

print(f"the number of visible trees is {np.sum(visible)}")