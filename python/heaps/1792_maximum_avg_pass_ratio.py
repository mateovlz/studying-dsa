"""
1792. Maximum Average Pass Ratio
Solved
Medium
Topics
Companies
Hint
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
 

Constraints:

1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105
"""

from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        maxHeap = []
        total_classes = len(classes)
        sum = 0.0
        def gain(p,t):
            return (p + 1) / (t + 1) - (p / t) 

        for p , t  in classes:
            sum += p / t
            heapq.heappush(maxHeap, (-gain(p,t), p, t))

        while extraStudents > 0:
            max_class = heapq.heappop(maxHeap)
            cur_gain, p , t = max_class
            sum -= p / t
            p_n = p + 1
            t_n = t + 1
            sum += p_n / t_n
            heapq.heappush(maxHeap, (-gain(p_n,t_n), p_n, t_n))

            extraStudents -= 1

        return sum / total_classes
    
sl = Solution()

print(sl.maxAverageRatio([[1,2],[3,5],[2,2]], 2))