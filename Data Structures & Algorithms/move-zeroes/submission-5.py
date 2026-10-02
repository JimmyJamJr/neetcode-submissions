class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        for b in range(len(nums)):
            if nums[b] != 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
        
