class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0                              # unreachable; also keeps the final index in range

        n = len(nums)
        width = 2 * total + 1                     # sums range from -total to +total
        # dp[i][s + total] = number of ways to reach sum s using the first i numbers
        dp = [[0] * width for _ in range(n + 1)]
        dp[0][total] = 1                          # sum 0 lives at column `total`

        for i in range(n):
            num = nums[i]
            for col in range(width):
                ways = dp[i][col]
                if ways == 0:
                    continue                      # sum not reachable after i numbers
                dp[i + 1][col + num] += ways      # choose +num
                dp[i + 1][col - num] += ways      # choose -num
        return dp[n][target + total]