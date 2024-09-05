

def check_for_target(nums,target):
    left = 0
    right = len(nums) -1 

    while left < right:
        current = nums[left] + nums[right]
        if current: return True
        if(current > target):
            right -= 1
        if(current < target):
            left -= 1
        
    return False

print(check_for_target([1, 2, 4, 6, 8, 9, 14, 15],13))