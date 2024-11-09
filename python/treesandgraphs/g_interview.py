

"""
Find each final point for every waterfall ([i][j]) in the m x n matrix
input = [
  [1,2,4],
  [3,5,8],
  [9,3,2]
]

"""

from collections import deque, defaultdict

def find_final_points(waterfall):
    #               East  West    South North
    directions = [(0,1), (0,-1), (1,0), (-1,0) ]
    
    def out_bounds(row,col):
        print(row, col)
        return row < 0 or row >= m or col < 0 or col >= n 
        #return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"
    
    def find_path(val,rowm, colm):
        foundSmallW = None
        outbounds = None
        small_one = defaultdict(None)
        smaller = float("inf")

        queue = deque([(rowm, colm)])

        while queue:
            row, col = queue.popleft()

            for dx, dy in directions:
                next_x, next_y = row + dx , col + dy
                
                if out_bounds(next_x, next_y):
                    outbounds = (next_x, next_y)
                    #print((next_x, next_y))
                else :
                    if waterfall[next_x][next_y] < val:
                        queue.append((next_x, next_y))
                        foundSmallW = (next_x, next_y)
                        smaller = min(smaller, waterfall[next_x][next_y])
                        small_one[waterfall[next_x][next_y]] = (next_x, next_y)

        if foundSmallW: 
            return small_one[smaller]
        
        if outbounds: 
            return outbounds
                    
    m = len(waterfall)
    n = len(waterfall[0])

    ans = [[0] * n for _ in range(m)]

    for x  in range(m):
        for y in range(n):
            ans[x][y] = find_path(waterfall[x][y], x, y)
    print(ans)


find_final_points([
  [1,2,4],
  [3,5,8],
  [9,3,2]
])

[[(2, -1), None, None], 
 [(2, -1), None, None], 
 [(2, -1), None, None]]