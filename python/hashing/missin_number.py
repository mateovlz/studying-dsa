

def missin_number(nums: list[int]):
    num_set = set(nums)
    n = len(nums) +1
    for number in range(n):
        if number not in num_set:
            return number
        
print(missin_number([3,0,1]))