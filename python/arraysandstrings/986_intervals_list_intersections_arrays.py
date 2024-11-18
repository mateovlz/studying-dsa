"""
986. Interval List Intersections
Solved
Medium
Topics
Companies
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109 
endj < startj+1
"""

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if firstList == [] or secondList == []:
            return []

        j = 0
        k = 0
        ans = []

        while j < len(firstList) and k < len(secondList):
            x, y = 0,0 
            jx = firstList[j][0]
            jy = firstList[j][1]
            kx = secondList[k][0]
            ky = secondList[k][1]
            if jx >= kx and jx <= ky:
                x = jx
            elif kx > jx and kx <= jy : 
                x = kx

            if jy <= ky and jy >=  kx:
                y = jy
                j += 1
                ans.append([x,y])
            elif ky < jy and ky >= jx: 
                y = ky
                k += 1
                ans.append([x,y])
            elif ky < jx:
                k+=1
            else:
                j+=1
        return ans
            


#improvement            
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []  # to store all intersecting intervals
        i = j = 0  # Initialize pointers for both lists

        # While both lists have unprocessed intervals
        while i < len(firstList) and j < len(secondList):
            # Calculate the start and end of the potential intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If there's a valid intersection, add it to the result list
            if start <= end:
                intersections.append([start, end])

            # Move forward in the list with the earlier ending interval
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections