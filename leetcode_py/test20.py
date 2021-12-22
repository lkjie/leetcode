
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''

class Solution:
    def generateParenthesis(self, n: int):
        def dfs(l, r, prefixs):
            if r < l:
                return []
            if l <= 0 and r <= 0:
                return prefixs
            elif l > 0 and r <= 0:
                return []
            elif l <= 0 and r > 0:
                return [s + ')'*r for s in prefixs]
            else:
                return dfs(l-1,r,[s+'(' for s in prefixs]) + dfs(l,r-1,[s+')' for s in prefixs])
        return dfs(n-1,n,["("])


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))