import numpy as np

data = open(r"input\06.txt", 'r')
inputdata = np.asarray([line.strip() for line in data])[0]

############################## PART 1 ##############################

for index in range(len(inputdata)-3):
    symbols = [c for c in inputdata[index:index+4]]
    if np.unique(symbols).shape[0] == 4:
        print(f"found marker at index {index+4}")
        break