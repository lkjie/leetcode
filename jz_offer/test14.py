# -*- coding:utf-8 -*-

def powmod(a,x,p):
    if x == 0:
        return 1
    res = 1
    for _ in range(x):
        res = (res * a) % p
    return res


class Solution:
    def cuttingRope(self, n: int) -> int:
        # dp
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return powmod(3,n//3,1000000007)
        elif n % 3 == 1:
            return powmod(3, n // 3 - 1, 1000000007) * 4
        else:
            return powmod(3, n // 3, 1000000007) * 2


if __name__ == '__main__':
    s = Solution()
    r = s.cuttingRope(120)
    print(r)