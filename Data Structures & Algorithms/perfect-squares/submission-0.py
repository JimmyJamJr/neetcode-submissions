class Solution:
    def numSquares(self, n: int) -> int:
        # DP[i] = min(DP[i - s^2] + 1) for all s^2 <= i
        # OPT = DP[n]

        dp = [0] + [float("inf")] * n 

        for i in range(n + 1):
            s = 1
            m = 1
            smallest = float("inf")
            while s ** 2 <= i:
                dp[i] = min(dp[i - s ** 2] + 1, dp[i])
                s += 1

        return dp[n]