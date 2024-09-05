from collections import defaultdict

def subarray_sum_has_prefix(nums:list[int], k:int):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
    return ans 


print(subarray_sum_has_prefix([1,2,1,2,1], 3));


