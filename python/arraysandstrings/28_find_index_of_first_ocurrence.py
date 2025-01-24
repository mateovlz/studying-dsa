"""
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
# O(h * m)  O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r, j = 0, 0, 0
        while r < len(haystack):
            if haystack[r] == needle[j]:
                if j == len(needle)-1:
                    return l
                j += 1
                r += 1
            else:
                j = 0
                l += 1
                r = l
        return -1