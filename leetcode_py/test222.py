
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter, defaultdict
from typing import List

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.h = None
        self.res = None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        h = 1
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                h += 1
            else:
                break

        def dfs(r, level):
            if self.res:
                return
            if level == h:
                self.res = r.val
            if r.right:
                dfs(r.right, level + 1)
            if r.left:
                dfs(r.left, level + 1)
        return self.res


if __name__ == '__main__':
    s = Solution()
    l = [["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]
    r = s.countNodes(l)
    print(r)
