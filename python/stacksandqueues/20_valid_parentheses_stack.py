"""
20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = { '(':')',  '[':']',  '{':'}'}

        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if not stack:
                    return False
                last_item = stack.pop()

                if matches[last_item] != c:
                    return False

        return not stack
