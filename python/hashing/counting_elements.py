

def counting_elements(arr):
    nums = set(arr)
        
    count = 0
    for x in nums:
            
        if x + 1 in nums:
            count+=1
    return count

print(counting_elements([1,2,3,4,4,6,7]))