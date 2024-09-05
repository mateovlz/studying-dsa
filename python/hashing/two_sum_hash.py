
def two_sum_hash(nums: list[int], target:int):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        comp = target - num 
        if (comp) in dic:
            return [ dic[comp], i ]
        dic[num] = i


print(two_sum_hash([5,2,7,10,3,9],8))