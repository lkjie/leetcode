
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter

c1 = Counter()
c2 = Counter()
print(c1)
print(c2)
print(c1 == c2)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 减法
        i = 0
        neg = 0
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            neg = 1
        if dividend < 0:
            dividend = -dividend
        if divisor  < 0:
            divisor = -divisor
        while dividend > divisor:
            dividend -= divisor
            i += 1
        return -i if neg else i



if __name__ == '__main__':
    s = Solution()
    print(s.divide(7, -3))