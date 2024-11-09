

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

    
    rows = len(waterfall)
    cols = len(waterfall[0])
    directions = [(0,1), (1,0), (0, -1), (-1,0)]

    ans_w = [ [0] * cols for _ in range(rows)]

    def is_outbounds(row, col):
        rows = len(waterfall)
        cols = len(waterfall[0])
        return row < 0 or row >= rows or col< 0 or col >= cols

    def find_path(x,y, val):
        queue = deque()
        ans = None
        last_position = None
        queue.append((x,y,val))

        while queue: 
            row, col , v = queue.popleft()
            last_position = (row, col)
            for dx, dy in directions:
                next_row, next_col = dx + row, dy + col
                if is_outbounds(next_row, next_col):
                    ans = (next_row, next_col)
                else:
                    #print(next_row, next_col)
                    next_val = waterfall[next_row][next_col]
                    if next_val < v:
                        queue.append((next_row, next_col, next_val ))
        if ans is None:
            return last_position
        return ans
        
    for row in range(rows):
        for col in range(cols):
            #print(find_path(row, col, waterfall[row][col]))
            ans_w[row][col] = find_path(row, col, waterfall[row][col])

    print(ans_w)
                    


find_final_points([
  [4,9,8,9,8],
  [9,7,6,5,9],
  [9,8,3,4,5],
  [6,10,5,7,5]
])

"""
  [1,2,4],
  [3,5,8],
  [9,3,2]

  [(0,-1), (0,-1), (0,-1)],  - [(-1, 0), (-1, 0), (-1, 0)]
  [(0,-1), (0,1),  (0,1)] - [(-1,0), (-1,0), (-1,0)]
  [(0,-1),(3,2), (3,2)] - [(-1,0),(2,3), (2,3) ] - [(2,3)]

  [4,3,8,9],
  [5,2,1,2],
  [6,7,4,3]

  [[(-1, 1), (-1, 1), (-1, 1), (-1, 1)], 
  [(-1, 1), (1, 2), (1, 2), (1, 4)], 
  [(-1, 1), (-1, 1), (1, 4), (1, 4)]]

  [4,9,8,9,8],
  [9,7,6,5,9],
  [9,8,3,4,5],
  [6,10,5,7,5]

  [[(-1, 0), (-1, 0), (-1, 2), (-1, 2), (-1, 4)], 
   [(-1, 0), (2, 2), (2, 2), (2, 2), (-1, 4)], 
   [(3, -1), (2, 2), (2, 2), (2, 2), (2, 5)], 
   [(3, -1), (3, -1), (4, 2), (4, 2), (4, 4)]]
"""