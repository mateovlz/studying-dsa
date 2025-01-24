
## BINARY SEARCH

from typing import List


b_ages = [1,2,3,4,5,6,7,9]
        # 0,1,2,3,4,5,6,7

"""
 ## DEBUGGING
 ith left right mid nums[mid]
 1    0   7     3     4 
 2    0   3     1     2
 3    2   3     2     3
 4    2   2 
"""
print("### Find Exact Value Position or Insertion Position IF Missed")
#find exact value or point of insertion (LEFT MOST)
def find_position_of_value_or_insertion_point_exact(nums, target):
    left = 0
    right = len(nums)-1
    #print("l r m vl")
    while left <= right:
        mid = (right + left)// 2
        #print(left, right, mid, nums[mid])
        if nums[mid] == target:
            #found position
            return mid
        elif nums[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1
    #found insertion point 
    return left

print(b_ages[find_position_of_value_or_insertion_point_exact(b_ages, 3)] == 3)
print(find_position_of_value_or_insertion_point_exact(b_ages, 9))
print(find_position_of_value_or_insertion_point_exact(b_ages, 7))
print(find_position_of_value_or_insertion_point_exact(b_ages, 8))


print("### Find the first ocurrence or the first position where can be inserted")
#find exact value or point of insertion (LEFT MOST)
#could find the first greatest nearest to the target 
def find_position_of_value_or_insertion_dupl(nums, target):
    left = 0
    right = len(nums)-1
    #print("l r m vl")
    while left < right:
        mid = (right + left)// 2
        #print(left, right, mid, nums[mid])
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    #found insertion point 
    return left

print(find_position_of_value_or_insertion_dupl(b_ages, 3))
print(find_position_of_value_or_insertion_dupl(b_ages, 9))
print(find_position_of_value_or_insertion_dupl(b_ages, 7))
print(find_position_of_value_or_insertion_dupl(b_ages, 8))

print("### Find first element greater than the target or where a target ends")
# most left
def find_position_of_value_greater(nums:List[int], target: int):
    left = 0
    right = len(nums) - 1
    print(target)
    print("l r m vl")
    while left < right:
        mid = (right + left)//2
        print(left, right, mid, nums[mid])
        #return 1
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1 
    return left

print(find_position_of_value_greater(b_ages, 2))
#print(find_position_of_value_greater(b_ages, 9))
#print(find_position_of_value_greater(b_ages, 7))
#print(find_position_of_value_greater(b_ages, 8))