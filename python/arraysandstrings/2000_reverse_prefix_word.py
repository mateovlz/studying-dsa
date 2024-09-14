"""te = l
                tmp = ""
                while te >= 0:
                    tmp += word[te]
                    te -=1
                ans = tmp
                found = True"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        r =len(word)
        l =0 
        ans = ""
        found = False

        if ch not in word:
            return word

        while l < r:
            if word[l] == ch and found is False:
                ans = word[0:l+1][::-1]
                found = True
            else:
                ans+= word[l]
            l += 1
        return ans
                

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        r =len(word)
        l =0 
        ans = ""
        found = False

        if ch not in word:
            return word
            
        while l < r:
            if word[l] == ch and found is False:
                te = l
                tmp = ""
                while te >= 0:
                    tmp += word[te]
                    te -=1
                ans = tmp
                found = True
            else:
                ans+= word[l]
            l += 1
        return ans
                
