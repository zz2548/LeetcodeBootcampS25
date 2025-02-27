class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        postfix = 1
        answer = [0] * n
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer