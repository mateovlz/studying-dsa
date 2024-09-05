def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = len(nums) -1
        res = [0] * n
        
        #  [-4,-1,0,3,10]
        
        for i in range(n-1, -1, -1 ):
            if(abs(nums[left])  > abs(nums[right]) ):
                square = nums[left]
                left+= 1
            else:
                square = nums[right]
                right -= 1
                
            res[i] = square * square
        return res

print(sortedSquares([-4,-1,0,3,10]))