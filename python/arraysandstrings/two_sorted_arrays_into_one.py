

def two_sorted_arrays_into_one(arr1:list[int], arr2:list[int]) -> list[int]:
    ans = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if(arr1[i] < arr2[j]):
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j+=1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans


print(two_sorted_arrays_into_one([1,4,7,20], [3,5,6]))