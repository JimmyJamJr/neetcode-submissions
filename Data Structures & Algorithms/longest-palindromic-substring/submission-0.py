class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r              # palindrome is s[l+1:r]

        start, end = 0, 0
        for i in range(len(s)):
            for l, r in (expand(i, i), expand(i, i + 1)):   # odd, even
                if r - l > end - start:
                    start, end = l, r
        return s[start:end]