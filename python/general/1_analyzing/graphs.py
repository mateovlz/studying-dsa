from collections import defaultdict, deque



## Array of edges

arrEdges = [[0,1],[1,2], [2,0], [2,3], [0,3]]

def traversing_arr_edges(arrEdges):
    print("Traversing array of edges")
    graph = defaultdict(list)
    #building graph matrix
    for x, y in arrEdges:
        graph[x].append(y)

    print(graph)

    for key, value in graph.items():
        print("The node {0} has -> relations with {1} ".format(key, value))





traversing_arr_edges(arrEdges)
print()
## Adjancency list

adjList = [[1], [2], [0,3]]

def traversing_adj_list(adjList):
    print("Traversing adjacency list")
    # we could traverse just right away dont need to pre-process
    for x in range(len(adjList)):
        print("The node {0} has -> relations with {1}".format(x, adjList[x]))

traversing_adj_list(adjList)
print()
## Adjancency matrix

adjMatrix = [
    [0,1,0,0],
    [0,0,1,0],
    [1,0,0,1],
    [0,0,0,0]
]

def traversing_adj_matrix(adjMatrix):

    print("Traversing adjacency matrix")
    graph = defaultdict(list)

    #iterate with one validating each col and row
    for c in range(len(adjMatrix)):
        for r in range(len(adjMatrix[c])):
            if adjMatrix[c][r] == 1:
                print("The node {0} has -> realtions with {1}".format(c, r))

    print("Building an adjacency list to iterate better on the logic")
    #build adjancency list
    for c in range(len(adjMatrix)):
        for r in range(len(adjMatrix[c])):
            if adjMatrix[c][r] == 1:
                graph[c].append(r)


    for key, value in graph.items():
        print("The node {0} has -> relations with {1}".format(key, value))
traversing_adj_matrix(adjMatrix)
print()
## Matrix

matrix = [
    [1,0,0,0],
    [1,1,0,0],
    [1,0,1,0],
    [0,0,0,1],
]
#Remember that with graphs problems we have to look a lot on the 
#problem description to know how to traverse or what to do?
# << For this  specific we want to find the number of islands and max islands connected>>
# This approach is using DFS to traverse the graph
def traversing_matrix_dfs(matrix):
    print("Traversing a matrix graph using DFS")
    m = len(matrix)
    n = len(matrix[0])
    ans = 0
    maxArea = 0
    seen = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(col, row):
        #return col > 0 and col <= m and row > 0 and row <= m
        return 0 <= col < m and 0 <= row < n and matrix[col][row] == 1

    def dfs(n_col, n_row):
        nums_island = 0

        #iterate the neighbors of the node on left - right - up - down directions
        for dx, dy in directions:
            col, row = dx + n_col, dy + n_row
            if is_valid(col, row) and (col, row) not in seen:
                seen.add((col, row))
                nums_island += dfs(col, row)
        return nums_island + 1
    
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            if matrix[c][r] == 1 and (c, r) not in seen:
                seen.add((c,r))
                ans_dfs = dfs(c, r)
                ans +=  ans_dfs
                print(ans_dfs, ans)
                maxArea = max(maxArea, ans_dfs)

    print("Total of island {0}".format(ans))
    print("Max area of island connected {0}".format(maxArea))

traversing_matrix_dfs(matrix)

matrix2 = [
    [1,0,0,0],
    [1,1,1,0],
    [0,0,1,1],
    [0,0,0,1],
]
#Remember that with graphs problems we have to look a lot on the 
#problem description to know how to traverse or what to do?
# << For this  specific we want to find the nearest exit the min number of steps to exit >>
# This approach is using BFS to traverse the graph
def traversing_matrix_bfs(matrix):
    print("Traversing a grpah matrix with BFS")

    cols = len(matrix)
    rows = len(matrix[0])
    # left - right - up - down
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    seen = set()
    queue = deque()

    seen.add((0,0))
    #             row, col  step
    queue.append((0, 0, 1))

    def is_valid(col, row):
        return 0 <= col < cols and 0 <= row < rows
    
    while queue:
        n_row, n_col, steps = queue.popleft()

        for dx, dy in directions:
            col, row = dx + n_col, n_row + dy
            if is_valid(col, row) and matrix[col][row] == 1 and (col, row) not in seen:
                if 0 == row or row == rows -1 or 0 == col or col  == cols - 1:
                    print("Steps to the exit {0}".format(steps + 1)) 
                
                seen.add((col, row))
                queue.append((col, row, steps + 1))

    return -1
                        
traversing_matrix_bfs(matrix2)
    

    