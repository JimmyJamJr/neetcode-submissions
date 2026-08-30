class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        l, r = 0, 0
        count = [0] * 26
        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1
            while max(count) + k < r - l + 1:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1  
            best = max(best, r - l + 1)
            r += 1

        return best
