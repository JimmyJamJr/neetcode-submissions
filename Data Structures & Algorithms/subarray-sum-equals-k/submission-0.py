class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prefix_count = {0: 1}

        sum = 0
        for num in nums:
            sum = sum + num
            if sum - k in prefix_count:
                subarrays += prefix_count[sum - k]
            prefix_count[sum] = prefix_count.get(sum, 0) + 1

        return subarrays
