# -*- coding:utf-8 -*-
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return True
        if not s:
            return False
        A = [[False for _ in range(0, len(p)+1)] for _ in range(0, len(s)+1)]
        A[0][0] = True
        def matchij(i,j):
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]
        for i in range(0, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    if matchij(i,j-1):
                        A[i][j] = A[i][j-2] or A[i-1][j]
                    else:
                        A[i][j] = A[i][j-2]
                else:
                    if matchij(i,j):
                        A[i][j] = A[i-1][j - 1]
                    else:
                        A[i][j] = False
        return A[-1][-1]


if __name__ == '__main__':
    s = Solution()
    r = s.isMatch("aa", "a*")
    print(r)