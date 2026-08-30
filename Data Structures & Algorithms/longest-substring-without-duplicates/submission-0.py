class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        a, b = 0, 0
        seen_chars = set()

        while b < len(s):
            while s[b] in seen_chars and a < b:
                seen_chars.remove(s[a])
                a += 1
            seen_chars.add(s[b])
            best = max(best, b - a + 1)
            b += 1
        return best


