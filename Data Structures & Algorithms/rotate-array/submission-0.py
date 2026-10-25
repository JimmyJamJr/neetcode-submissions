class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        
        def reverse_inplace(numbers, a, b):
            while a < b:
                numbers[a], numbers[b] = numbers[b], numbers[a]
                a += 1
                b -= 1
        
        reverse_inplace(nums, 0, len(nums) - 1)
        reverse_inplace(nums, 0, k - 1)
        reverse_inplace(nums, k, len(nums) - 1)

