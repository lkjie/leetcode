
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter, defaultdict
from typing import List

from collections import defaultdict

class LinkNode:
    def __init__(self, isleaf=False):
        self.isleaf = isleaf
        self.next = defaultdict(LinkNode)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        nrows, ncols = len(matrix), len(matrix[0])
        A = [[0 for _ in range(0, ncols)] for _ in range(0, nrows)]
        # for i in range(0, nrows):
        #     accum = 0
        #     for j in range(0, ncols):
        #         if matrix[i][j] == '0':
        #             accum = 0
        #         else:
        #             accum += int(matrix[i][j])
        #         A[i][j] = accum
        # res = 0
        # for col in range(0, ncols):
        #     elow = [-1 for _ in range(0, nrows)]
        #     ehigh = [nrows for _ in range(0, nrows)]
        #     s = []
        #     for i in range(0, nrows):
        #         while s and s[-1][0] >= A[i][col]:
        #             ehigh[s[-1][1]] = i
        #             s.pop(-1)
        #         if s:
        #             elow[i] = s[-1][1]
        #         s.append((A[i][col], i))
        #     for i in range(0, nrows):
        #         h = A[i][col]
        #         w = ehigh[i] - elow[i] - 1
        #         size = min(h,w)
        #         res = max(res, size*size)
        # return res
        res = 0
        for i in range(0, nrows):
            for j in range(0, ncols):
                if i == 0 or j == 0:
                    if matrix[i][j] == 1:
                        A[i][j] = 1
                else:
                    if matrix[i][j] == 1:
                        A[i][j] = min(A[i-1][j], A[i][j-1], A[i-1][j-1]) + 1
                res = max(res, A[i][j]*A[i][j])
        return res

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    s = Solution()
    l = [["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]
    r = s.maximalSquare(l)
    print(r)
