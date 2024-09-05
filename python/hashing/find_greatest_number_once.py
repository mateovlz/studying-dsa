

def largestUniqueNumber(self, nums: List[int]) -> int:
    counts = defaultdict(int)
    ans = -1
    for i in range(len(nums)):
        counts[nums[i]] += 1
    
    for key, value in counts.items():
        if value==1:
            ans = max(ans, key)
    return ans

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))