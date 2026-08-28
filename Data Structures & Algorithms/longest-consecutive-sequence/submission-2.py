class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        best = 0
        for n in uniques:
            if n - 1 not in uniques:
                # new chain
                length = 1
                while n + length in uniques:
                    length += 1
                best = max(best, length)
        
        return best


