

def subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    left = ans = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]

        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1
    return ans

print(subarray_product_less_than_k([10, 5, 2, 6], 100))