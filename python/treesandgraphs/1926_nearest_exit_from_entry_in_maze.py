"""
1926. Nearest Exit from Entrance in Maze
Solved
Medium
Topics
Companies
Hint
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
 
"""


from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows = len(maze)
        cols = len(maze[0])

        directions = [(-1,0), (1,0), (0, -1), (0,1)]
        queue = deque()
        seen = set()
        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols

        queue.append((entrance[0],entrance[1], 0))
        seen.add((entrance[0],entrance[1]))

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                next_row, next_col = dx + row, dy + col
                print(next_row, next_col)
                if is_valid(next_row, next_col) and maze[next_row][next_col] == '.' and (next_row, next_col) not in seen:
                    if 0 == next_row or next_row == rows -1 or 0 == next_col or next_col == cols -1:
                        return steps + 1

                    queue.append((next_row, next_col, steps + 1))
                    seen.add((next_row, next_col))
        return -1