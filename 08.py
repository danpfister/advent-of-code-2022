import numpy as np

data = open(r'input\08.txt', 'r')
inputdata = np.asarray([[int(c) for c in line.strip()] for line in data])

############################## PART 1&2 ##############################

visible = np.zeros_like(inputdata, dtype=bool)
scenic_score = np.empty_like(inputdata)

for row in range(inputdata.shape[0]):
    for tree in range(inputdata.shape[1]):
        current_tree = inputdata[row][tree]
        orientations = [inputdata[:row, tree][::-1], inputdata[row, :tree][::-1], inputdata[row+1:, tree], inputdata[row, tree+1:]] # counter clockwise starting from upwards
        view_distances = np.empty(4)
        for index, orientation in enumerate(orientations):
            current_view_distance = 0
            for next_tree in orientation:
                current_view_distance += 1
                if next_tree >= current_tree:
                    break
            view_distances[index] = current_view_distance
            if np.all(orientation < current_tree):
                visible[row][tree] = True
        scenic_score[row][tree] = np.prod(view_distances)

print(f"the number of visible trees is {np.sum(visible)}")
print(f"the tree at position {np.argwhere(scenic_score == np.max(scenic_score))[0]} has the overall maximum scenic score {np.max(scenic_score)}")