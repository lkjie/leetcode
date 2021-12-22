
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
        self.pathp = None
        self.pathq = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(r, fathers):
            if not r:
                return
            fathers.append(r)
            if r == p:
                self.pathp = fathers
            if r == q:
                self.pathq = fathers
            if self.pathp and self.pathq:
                return
            dfs(r.left, fathers)
            dfs(r.right, fathers)
            fathers.pop(-1)
        dfs(root, [])
        for i in range(len(self.pathp)-1, -1, -1):
            for j in range(len(self.pathq)-1, -1, -1):
                if self.pathp[i] == self.pathq[j]:
                    return self.pathp[i]
        return root


if __name__ == '__main__':
    s = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p1.left = p2
    p1.right = p3
    p2.right = p4
    r = s.lowestCommonAncestor(p1,p4,p1)
    print(r)
