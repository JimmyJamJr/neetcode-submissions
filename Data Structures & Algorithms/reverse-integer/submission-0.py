class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2 ** 31 - 1, -2 ** 31
        result = 0
        sign = 1 if x > 0 else -1
        x *= sign
        while x != 0:
            if result > MAX / 10 or result < MIN / 10:
                return 0

            result = result * 10 + x % 10
            x = x // 10
        
        return result * sign