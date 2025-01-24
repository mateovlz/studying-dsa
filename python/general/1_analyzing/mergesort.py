






#lets sort an array using merge sort 


# The main idea is to divide an conquer
#   We should divide the array in two pieces and 

"""
    [3,1,4,5,6,7,8,9]
    left  [3,1,4,5]
    right [6,7,8,9]
        LEFT
            left  [3,1]
            right [4,5]
                
        RIGHT
            left [6,7]
            right [8,9]

"""




def sort():
    arr = [3,1,4,5,6,7,8,9,3]
    l = 0
    r = len(arr)-1

    merge_sort(arr, l, r)
    print(arr)

#this function help us dividing the array in pieces
def merge_sort(arr, l, r):
    if l == r:
        return arr
    # the idea is to sort each division
    #LEFT ARR - RIGHT ARR
    mid = (l + r) // 2
    merge_sort(arr, l , mid)
    merge_sort(arr, mid+1, r)

    merge(arr, l, mid, r)
    return arr

#will help defining whats bigger or smaller and sort the items
def merge(arr, l, m, r):
    #we gather each left and right array
    left_arr, right_arr = arr[l:m+1], arr[m+1: r+1]
    #the idea is to sort this two arrays
    #left  [3,1]   right [4,5]
    
    #Have in mind this sorting is going to be on place 
    #so we need 
    ### one iterator for the main array and 
    #### other 2 for the | left_arr and right_arr|
    i, j, k = l, 0, 0
    print(arr[l:r+1],left_arr, right_arr)
    while j < len(left_arr) and k < len(right_arr):
        #lets validate which one is greater than the other and update the 
        if left_arr[j] <= right_arr[k]:
            arr[i] = left_arr[j]
            j += 1 
        else:
            arr[i] = right_arr[k]
            k += 1
        i += 1

    while j < len(left_arr):
        arr[i] = left_arr[j]
        j += 1
        i += 1

    while k < len(right_arr):
        arr[i] = right_arr[k]
        k += 1
        i += 1

    """
        [3,1,4,5]
        
        [3,1,4,5] 6,7,8,9]




        [6,7,8,9]
        [6,7,8,9]
    """

sort()