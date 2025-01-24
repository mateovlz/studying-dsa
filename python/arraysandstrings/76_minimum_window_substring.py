"""
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""

        count_t, window = defaultdict(int), defaultdict(int)
        #lets count t
        for i in range(len(t)):
            count_t[t[i]] += 1

        ans, ans_len = [-1,-1], float("inf")
        have, need= 0, len(count_t) 
        left = 0
        for right in range(len(s)):
            c = s[right]

            if c in count_t:
                window[c] += 1
                if c in count_t and window[c] == count_t[c]:
                    have += 1
            
            while have == need:
                if (right - left + 1) < ans_len:
                    ans = [left, right]
                    ans_len = (right - left + 1)
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1

        l, r = ans
        return s[l:r+1]
