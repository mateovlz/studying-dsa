

def longest_subarray_sum(nums, k:int) -> int:
    left = 0
    right = 0
    curr = 0 
    ans = 0

    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans

print(longest_subarray_sum([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))