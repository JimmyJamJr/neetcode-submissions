class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = 0
        b = len(s) - 1
        while a < b:
            while a < b and not s[a].isalnum():
                a += 1
            while a < b and not s[b].isalnum():
                b -= 1
            if s[a] != s[b]:
                return False
            a, b = a + 1, b - 1
        return True