


def best_subarray_w_fixed_wind(nums, k):
    curr = 0

    #Creating the first window
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        print(i)
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    return ans

print(best_subarray_w_fixed_wind([3,-1, 4, 12, -8, 5, 6], 4))