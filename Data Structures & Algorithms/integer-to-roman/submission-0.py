import math
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I"
        }

        mapping_special = {
            900: "CM",
            400: "CD",
            90: "XC",
            40: "XL",
            9: "IX",
            4: "IV"
        }

        output = ""

        while num > 0:
            first_digit = num // 10 ** int(math.log10(num))
            chosen_k, chosen_v = None, None
            for k, v in mapping.items() if first_digit != 4 and first_digit != 9 else mapping_special.items():
                if k <= num:
                    chosen_k, chosen_v = k, v
                    break
            output += chosen_v
            num -= chosen_k
        
        return output


