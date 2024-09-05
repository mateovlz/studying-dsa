from collections import defaultdict

def intersection_mul_arrays(nums):
    counts = defaultdict(int)
    for arr in nums:
        for x in arr:
            counts[x] += 1

    n = len(nums)
    ans = []
    for key in counts:
        if counts[key] == n:
            ans.append(key)
    
    return sorted(ans)

print(intersection_mul_arrays([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))