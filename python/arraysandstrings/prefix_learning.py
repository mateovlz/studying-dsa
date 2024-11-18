


def building_prefix(nums, target):
    prefix = [nums[0]]


    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    #Getting the sum (could be multiplication) of all the element up to target index
    print("Getting sum up to target:")
    print(prefix[target])

    #Getting the sum within range of the elements
    print("Getting sum of values within a range:")
    print(prefix[3], prefix[1])
    print(prefix[3] - prefix[1] + nums[1]) # 9

    print(prefix[3] - prefix[0] ) # 9
    print("Getting sum of values within a range:")
    print(prefix[5] - prefix[3] + nums[3]) # 15
    print(prefix[5] - prefix[2]) # 15   i  - (j-1)
    


    return prefix


print(building_prefix([1,2,3,4,5,6,7,8], 2))