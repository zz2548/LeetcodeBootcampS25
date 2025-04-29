class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Brute force
        # Calculate sum of all subarrays, keep track of the maximum
        # 2. DP
        # When to keep negative numbers?
        # Keep any subarray with positive sum
        max_subarray = current_subarray = nums[0]
        for n in nums[1:]:
            current_subarray = max(n, current_subarray + n)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray