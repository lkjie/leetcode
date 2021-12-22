


class Solution:
    def romanToInt(self, s: str) -> int:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        r_digits = {v: k for k, v in digits}
        res = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in r_digits:
                res += r_digits[s[i:i+2]]
                i += 1
            else:
                res += r_digits[s[i]]
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("IV"))