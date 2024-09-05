

def check_is_palindrome(s:str):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    return True

print(check_is_palindrome("racecar"))
print(check_is_palindrome("racecarsa"))