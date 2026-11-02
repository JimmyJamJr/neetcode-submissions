class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP[a] = fewest coin possible to make amount a
        DP = [0] + [float("inf")] * amount
        for i in range(1, len(DP)):
            for coin in coins:
                if coin > i:
                    continue
                
                DP[i] = min(DP[i], 1 + DP[i - coin])
        return DP[amount] if DP[amount] != float("inf") else -1


