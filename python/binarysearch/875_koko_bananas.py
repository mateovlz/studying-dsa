"""

875. Koko Eating Bananas
Medium
Topics
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109


"""

#Analysis

#There are n piles of bananas piles = [3,6,7,11], 
# Koko has a limited hours h = 8 while the guards are away
# Koko can decide the # of bananas she can eat by hour being this k

#Help Koko decide What speed k, she should use to eat all the bananas 
# while the guards are away??


"""
The idea of the binary search for solutions spaces
is to (what is the max/min that something can be done?)

we could have a function that know if the task it's posible or not

You will have to separated the logic of array only with it's posible or not
and your aux function will help you define that.

"""

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)
            
            return hours <= h
        
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
    
sol = Solution()

print(sol.minEatingSpeed([3,6,7,11],8))