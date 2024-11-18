"""
912. Sort an Array
Solved
Medium
Topics
Companies
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


def sortArray(nums):

    def merge(arr, L, M, R):
        # remember that the left side is not inclusive
        left, right = arr[L:M+1], arr[M+1:R+1]
        i, j , k = L, 0, 0
        # step 3 
        # validate which value is greater to replace in place in the array
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        # when one of the arrays its completed we have to ensure 
        # the other one is fully iterate we dont know which one
        # should end first we both for the two
        while j < len(left):
            arr[i] = left[j]
            j += 1
            i+=1
            
        while k < len(right):
            arr[i] = right[k]
            k += 1
            i+=1


    # Divide the array in pieces
    def mergeSort(arr, l, r):
        if l == r:
            return arr
        
        m =  (l + r) // 2
        # executed the divide an conquer for each half recurisvely
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)

        # finally merge both each half sorted
        merge(arr, l, m, r)

        return arr
    
    return mergeSort(nums, 0, len(nums)-1)

print(sortArray([5,2,3,3,4,2,6,7,7,8,8,1]))