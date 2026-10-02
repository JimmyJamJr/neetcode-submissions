class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True
        
        reverse = 0
        copy = x
        while copy > 0:
            digit = copy % 10
            copy = copy // 10
            reverse = reverse * 10 + digit
        
        return reverse == x
