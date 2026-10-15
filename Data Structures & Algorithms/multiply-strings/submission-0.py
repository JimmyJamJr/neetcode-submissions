class Solution:    
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num2[j]) - ord('0')) * (ord(num1[i]) - ord('0'))
                total = result[i + j + 1] + product
                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        k = 0
        while k < m + n and result[k] == 0:
            k += 1
        
        return "".join(str(d) for d in result[k:])


