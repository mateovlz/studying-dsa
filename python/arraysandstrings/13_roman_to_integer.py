"""
    13. Roman to Integer
Solved
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

"""
front - back
    M  - >  1000
    C - > ? 
    M -> CM -> 900
    X -> ? -> 10 
    C -> XC -> 90
    I -> ? -> 1
    V - IV -> 4

    1000 + 900 + 90 + 4 = 1994
"MCMXCIV"
    back - front

    V -> 5
    I -> 1 but last one was V -> IV ->  -1
    C -> 100
    X -> but last one was C -> CX -> -10
    M -> 1000
    C -> but last one was M -> CM -> -100
    M -> 1000

    5 - 1 = 4
    100 - 10 = 90
    1000 - 100 = 900
    1000
    
    1000 + 900 + 90 + 4 = 1994
"""  

# back to front solution
# TC O(n) SC O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        #Given a Roman number in string -> number
        roman_numbers = {
            "I": 1,
            "IV": -1, # 4
            "V": 5,
            "IX": -1, # 9
            "X": 10,
            "XL": -10, # 40
            "L": 50,
            "XC": -10, # 90
            "C": 100,
            "CD": -100, # 400
            "D": 500,
            "CM": -100, # 900
            "M": 1000
        }

        # Remember that roman numbers are sorted by 
        # Largest to Smallest

        #roman numbers from 0 up to 3900
        ans = roman_numbers[s[len(s)-1]]
        for i in range(len(s)-2, -1, -1):
            if s[i] in roman_numbers:
                    if s[i] + s[i+1] in roman_numbers:
                        ans += roman_numbers[ s[i] + s[i+1] ]
                    else:
                        ans += roman_numbers[s[i]]
        return ans
    

# TC O(n) ) O(1)
# But slightly better
class Solution:
    def romanToInt(self, s: str) -> int:
        #Given a Roman number in string -> number
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Remember that roman numbers are sorted by 
        # Largest to Smallest

        #roman numbers from 0 up to 3900
        # " MCMXCIV "
        n = len(s)
        i = 0
        ans = 0
        
        while i < n:
            #We should validate that the current positions is smaller than the upcoming if not we should substract 
            #the smaller one to the largest
            
            if i + 1 < n  and roman_numbers[s[i]] < roman_numbers[s[i + 1]]:
                ans += roman_numbers[s[i + 1]] - roman_numbers[s[i]] 
                i += 2
            else:
                ans += roman_numbers[s[i]]
                i += 1

        return ans