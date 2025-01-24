"""
Encode and Decode Strings
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        left = 0
        for word in strs:
            ans.append("{}#{}".format(len(word), word))
        print("".join(ans))
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        i = 0
        ans =[]
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
   
            length = int(s[i:j])

            word = s[j+1: j + length + 1]
        
            ans.append(word)
            i = j + length + 1 
        return ans
