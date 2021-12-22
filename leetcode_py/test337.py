from typing import List
from collections import Counter, defaultdict
import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        chdnum = {}
        def dfs(node):
            if node is None:
                return 0
            # dont rob node
            lc = dfs(node.left)
            rc = dfs(node.right)
            nc1 = lc+rc
            nc2 = node.val + (chdnum.get(node.left.right,0) if node.left else 0) + (chdnum.get(node.left.left,0) if node.left else 0) + (chdnum.get(node.right.right,0) if node.right else 0) + (chdnum.get(node.right.left,0) if node.right else 0)
            nc = max(nc1, nc2)
            chdnum[node] = nc
            return nc
        return dfs(root)


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(3)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(3)
    t5 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    t3.right = t5
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.rob(t1)
    # 174801674
    print(r)
