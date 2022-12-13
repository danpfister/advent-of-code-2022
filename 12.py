import numpy as np

inputfile = open(r".\input\12.txt", 'r')
inputdata = np.asarray([[c for c in line.strip()] for line in inputfile])

############################## PART 1 ##############################

start = np.argwhere(inputdata == 'S')[0]
end = np.argwhere(inputdata == 'E')[0]
inputdata[start[0]][start[1]] = 'a'
inputdata[end[0]][end[1]] = 'z'
distances = np.zeros_like(inputdata, dtype=np.int32)

def bfs(inputdata, start, end, distances):
    visited = np.zeros_like(inputdata, dtype=bool)
    visited[start[0]][start[1]] = True
    queue = [start]

    distances[start[0]][start[1]] = 0
    while len(queue) > 0:
        current = queue.pop(0)

        if np.array_equal(current, end):
            return distances[current[0]][current[1]]
            break

        for neighbor in np.asarray([current + direction for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]]):
            if neighbor[0] not in range(inputdata.shape[0]) or neighbor[1] not in range(inputdata.shape[1]): # check if neighbor out of bounds
                continue
            if ord(inputdata[neighbor[0]][neighbor[1]]) > ord(inputdata[current[0]][current[1]]) + 1: # check if neighbor not too high
                continue
            current_visit = np.zeros_like(visited, dtype=bool); current_visit[neighbor[0]][neighbor[1]] = True
            if np.any(np.bitwise_and(visited, current_visit)): # check if already visited
                continue
            distances[neighbor[0]][neighbor[1]] = distances[current[0]][current[1]] + 1
            visited = np.bitwise_or(visited, current_visit)
            queue.append(neighbor)
        
        #print(distances)

print(f"found shortest path from current position with distance {bfs(inputdata, start, end, distances)}")

def reverse_bfs(inputdata, start):
    visited = np.zeros_like(inputdata, dtype=bool)
    visited[start[0]][start[1]] = True
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)

        if inputdata[current[0]][current[1]] == 'a':
            return current

        for neighbor in np.asarray([current + direction for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]]):
            if neighbor[0] not in range(inputdata.shape[0]) or neighbor[1] not in range(inputdata.shape[1]): # check if neighbor out of bounds
                continue
            if ord(inputdata[neighbor[0]][neighbor[1]]) < ord(inputdata[current[0]][current[1]]) - 1: # check if neighbor not too high
                continue
            current_visit = np.zeros_like(visited, dtype=bool); current_visit[neighbor[0]][neighbor[1]] = True
            if np.any(np.bitwise_and(visited, current_visit)): # check if already visited
                continue
            visited = np.bitwise_or(visited, current_visit)
            queue.append(neighbor)
    raise Exception("end was never reached!")

distances = np.zeros_like(inputdata, dtype=np.int32)
print(f"found shortest path from any a with distance {bfs(inputdata, reverse_bfs(inputdata, end), end, distances)}")