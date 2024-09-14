"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n= len(s)-1
        ans =""
        l = 0
        j = 0
        r = n
        k = n
        while l <= r:
            if s[l].isalpha() is True:
                val = s[k-j]
                while val.isalpha() is not True:
                    k -= 1
                    val = s[k-j]
                ans += val
                j += 1
            else :
                ans += s[l]
            l += 1
            
        return ans