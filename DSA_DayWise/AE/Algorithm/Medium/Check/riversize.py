
def riverSize(matrix):
    sizes = []
    visited = [[False for value in row]for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNode(i,j,visited,matrix,sizes)
    return sizes

def traverseNode(i,j,visited,matrix,sizes):
    currentsize = 0
    nodetoExplore = [[i,j]]
    while len(nodetoExplore):
        currentNode = nodetoExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentsize +=1
        unvisitedNeighbour = getunvisitedNeighbour(i,j,matrix,visited)
        for neighbour in unvisitedNeighbour:
            nodetoExplore.append(neighbour)
    sizes.append(currentsize)

def getunvisitedNeighbour(i,j,matrix,visited):
    unvisitedNeighbour = []
    if i>0 and not visited[i-1][j]:
        unvisitedNeighbour.append([i-1,j])
    if i<len(matrix)-1 and not visited[i+1][j]:
        unvisitedNeighbour.append([i+1,j])
    if j>0 and not visited[i][j-1]:
        unvisitedNeighbour.append([i,j-1])
    if j<len(matrix[0])-1 and not visited[i][j+1]:
        unvisitedNeighbour.append([i,j+1])
    return unvisitedNeighbour


if __name__ == "__main__":
    #arr = [[1,1],[1,1]]
    arr = [[1,0,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[0,0,1,0,1],[1,0,0,0,1]]
    total = riverSize(arr)
    print(total)


