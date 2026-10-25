class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        best_prev = nums[0]
        for i in range(1, len(nums)):
            best_prev = max(best_prev + nums[i], nums[i])
            best = max(best, best_prev)
        return best