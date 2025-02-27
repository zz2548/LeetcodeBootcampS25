class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive
        '''
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]
        '''
        i, j = 0, len(nums) - 1

        while (nums[i] + nums[j] != target):
            if nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]
