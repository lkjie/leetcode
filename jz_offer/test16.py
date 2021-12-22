# -*- coding:utf-8 -*-

def powmod(a,x,p):
    if x == 0:
        return 1
    res = 1
    for _ in range(x):
        res = (res * a) % p
    return res
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -1 * n
        if n <= 5:
            res = 1
            for _ in range(0, n):
                res = res * x
            return res
        else:
            if n % 2 == 0:
                return self.myPow(x*x,n//2)
            else:
                return self.myPow(x*x,(n-1)//2) * x


if __name__ == '__main__':
    s = Solution()
    r = s.myPow(2.10000, 3)
    print(r)