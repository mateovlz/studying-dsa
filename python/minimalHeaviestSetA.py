def minimalHeaviestSetA(arr):
    # Step 1: Sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Step 2: Initialize the subsets and their sums
    A = []
    sum_A = 0
    total_sum = sum(arr)
    
    # Step 3: Greedily add items to A until its sum exceeds half of the total sum
    for weight in sorted_arr:
        A.append(weight)
        sum_A += weight
        if sum_A > total_sum - sum_A:
            break
    
    # Step 4: Return A sorted in increasing order
    return sorted(A)

# Test case
arr = [3, 7, 5, 6, 2]
print(minimalHeaviestSetA(arr))  # Output: [6, 7]
