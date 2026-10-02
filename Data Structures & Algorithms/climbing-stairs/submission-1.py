class Solution:
    def climbStairs(self, n: int) -> int:
        # DP[i] = the number of ways to reach step i + 1
        DP = [0] * n
        
        for i in range(n):
            if i <= 1:
                DP[i] = i + 1
                continue

            DP[i] = DP[i - 2] + DP[i - 1]
        
        return DP[n - 1]
