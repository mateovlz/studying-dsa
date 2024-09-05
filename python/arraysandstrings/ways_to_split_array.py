
def ways_to_split_array(nums):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if(left_section >= right_section):
            ans += 1
            
    return ans

def waysToSplitArray(nums: list[int]) -> int:
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1

    return ans
    
print(ways_to_split_array([10,4,-8,7]))

print(waysToSplitArray([10,4,-8,7]))