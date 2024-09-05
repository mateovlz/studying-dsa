def getAverages(nums: list[int], k: int) -> list[int]:
        windows_size = 2*k + 1
        n = len(nums)
        
        if k == 0:
            return nums
        
        averages = [-1] * n
        if windows_size > n:
            return averages
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(k, n - k):
            averages[i] = (prefix[i+ k + 1] - prefix[i-k])//windows_size
        
        return averages

print(getAverages([7,4,3,9,1,8,5,2,6], 3))