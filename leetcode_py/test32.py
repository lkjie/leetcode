
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1 or (len(s) == 2 and s != '()'):
            return 0
        if len(s) == 2 and s == '()':
            return 2
        A = [0 for _ in range(0, len(s))]
        if s[0:2] == '()':
            A[1] = 2
        for i in range(2, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    A[i] = A[i-2] + 2
                else:
                    if i-A[i-1]-1 >= 0 and s[i-A[i-1]-1] == '(':
                        if i-A[i-1]-2 >= 0:
                            A[i] = A[i-1] + 2 + A[i-A[i-1]-2]
                        else:
                            A[i] = A[i - 1] + 2
                    else:
                        A[i] = 0
            else:
                A[i] = 0
        return max(A)

if __name__ == '__main__':
    s = Solution()
    l = [1,3,2]
    r = s.longestValidParentheses(")()())")
    print(r)
