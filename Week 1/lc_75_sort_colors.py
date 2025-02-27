class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket sort since we only have 3 values?
        # Achievable in O(n) time
        # We want to make sure l and r encapsulate 1
        i, l, r = 0, 0, len(nums) -1

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1