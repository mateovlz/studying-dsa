

def longest_substring_flipping(s:str):
    left = curr = ans = 0

    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
            
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
        
    return ans
    
print(longest_substring_flipping("110010111"))