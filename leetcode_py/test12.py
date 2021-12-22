class Solution:
    def intToRoman(self, num: int) -> str:
        str_num = str(num)
        res = ''
        for i in range(0, len(str_num)):
            loc = len(str_num) - i
            if loc == 4:
                res += int(str_num[i]) * 'M'
            if loc == 3:
                if str_num[i] == '9':
                    res += 'CM'
                elif str_num[i] >= '5':
                    res += 'D' + (int(str_num[i]) - 5) * 'C'
                elif str_num[i] == '4':
                    res += 'CD'
                else:
                    res += int(str_num[i]) * 'C'
            if loc == 2:
                if str_num[i] == '9':
                    res += 'XC'
                elif str_num[i] >= '5':
                    res += 'L' + (int(str_num[i]) - 5) * 'X'
                elif str_num[i] == '4':
                    res += 'XL'
                else:
                    res += int(str_num[i]) * 'X'
            if loc == 1:
                if str_num[i] == '9':
                    res += 'IX'
                elif str_num[i] >= '5':
                    res += 'V' + (int(str_num[i]) - 5) * 'I'
                elif str_num[i] == '4':
                    res += 'IV'
                else:
                    res += int(str_num[i]) * 'I'
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(58))