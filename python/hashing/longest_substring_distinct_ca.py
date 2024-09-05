from collections import defaultdict
"""
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
"""

def longest_substring_distinct_ca(s:str, k:int):
    counts = defaultdict(int)
    ans = left =0

    for right in range(len(s)):
        counts[s[right]] += 1

        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
    return ans


print(longest_substring_distinct_ca("eceba", 2))