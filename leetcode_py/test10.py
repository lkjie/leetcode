class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        A = [[False for j in range(0, len(p)+1)] for i in range(0, len(s)+1)]
        A[0][0] = True
        def match(i, j):
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]
        for i in range(0, len(s)+1):
            for j in range(1, len(p)+1):
                if(p[j-1]!='*'):
                    if match(i, j):
                        A[i][j] = A[i-1][j-1]
                    else:
                        A[i][j] = False
                else:
                    if match(i, j-1):
                        A[i][j] = A[i-1][j] or A[i][j-2]
                    else:
                        A[i][j] = A[i][j-2]
        return A[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('a', '.*'))