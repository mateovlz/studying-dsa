
def test_mate(related):
    def dfs(node, visited, M):
        for neighbor, isConnected in enumerate(M[node]):
            if isConnected and not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor, visited, M)

    # Convert the given matrix of strings to a list of lists of integers
    M = [list(map(int, list(row))) for row in related]

    n = len(M)
    visited = [False] * n
    groups = 0

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i, visited, M)
            groups += 1

    return groups

def count_groups(arr):
    def dfs(node,visited, m):
        print(f'node {node} {visited}')
        print(m[node])
        print(list(enumerate(m[node])))
        for neighbor, isConnected in enumerate(m[node]):
            print(f' neighbor {neighbor} connected {isConnected}')
            if isConnected and not visited[neighbor]:
                visited[neighbor] = True
                print(f' neighbor {neighbor} {visited}')
                dfs(neighbor, visited, m)
    
    m = [list(map(int, row.split(","))) for row in arr]
    print(m)
    n = len(m)
    visited = [False] * n
    groups = 0
    groups_l = [0] 
    print(visited)
    print("-----")
    for row in range(n):
        if not visited[row]:
            visited[row] = True
            dfs(row, visited, m)
            groups += 1
    print(groups)



if __name__ == "__main__":
    """count_groups(["1, 1, 0",
                  "1, 1, 0",
                  "0, 0, 1"])"""
    print(test_mate([
    "1100",
    "1110",
    "0110",
    "0001"
]))

"""
   0  1  2
0 "1, 1, 0",
1 "1, 1, 0",
2 "0, 0, 1"


["1,1,0,0",
               "1,1,1,0",
               "0,1,1,0",
               "0,0,0,1"]                  

   0 1 2 3
0 "1 1 0 0"
1 "1 1 1 0"
2 "0 1 1 0"
3 "0 0 0 1"
"""


