class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Example 1: total = 22, we try to see if we can get two partitions of 22/2 = 11 = target
        if sum(nums) % 2:
            return False
        dp = set() # Use a set to track the numbers we use
        dp.add(0)
        target = sum(nums) // 2 # Target should be exactly half

        # i starts from the end, go to 0
        for i in range(len(nums) -1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False