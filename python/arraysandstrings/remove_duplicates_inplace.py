def remove_duplicates_in_place(nums):
    seen = set()
    write_index = 0  # Pointer to the position for non-duplicate elements

    for read_index in range(len(nums)):
        if nums[read_index] not in seen:
            seen.add(nums[read_index])
            nums[write_index] = nums[read_index]
            write_index += 1
    print(nums)

    return nums[:write_index]  # Slice to keep only unique elements

# Example usage
nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates_in_place(nums))  # Output: [1, 2, 3, 4, 5]