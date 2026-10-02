import math
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"), (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")]

        output = ""

        while num > 0:
            chosen_k, chosen_v = None, None
            for k, v in mapping:
                if k <= num:
                    chosen_k, chosen_v = k, v
                    break
            output += chosen_v
            num -= chosen_k
        
        return output


