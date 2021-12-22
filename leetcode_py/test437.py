from collections import Counter, defaultdict
import copy
from leetcode_py.test297 import Codec
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> int:
#         fathermap = {}
#         if not root:
#             return 0
#
#         def dfs1(n):
#             if n.left:
#                 fathermap[n.left] = n
#                 dfs1(n.left)
#             if n.right:
#                 fathermap[n.right] = n
#                 dfs1(n.right)
#
#         def dfs2(n):
#             if not n:
#                 return
#             if n != root:
#                 n.val += fathermap[n].val
#             if n.left:
#                 dfs2(n.left)
#             if n.right:
#                 dfs2(n.right)
#
#         def dfs4(n, r):
#             # n 与 r的差
#             if not n:
#                 return 0
#             rcnt, lcnt = 0, 0
#             if n == r:
#                 ncnt = 0
#             else:
#                 ncnt = 1 if n.val - r.val == targetSum else 0
#             if n.left:
#                 lcnt = dfs4(n.left, r)
#             if n.right:
#                 rcnt = dfs4(n.right, r)
#             return ncnt + lcnt + rcnt
#
#         def dfs3(n):
#             rcnt, lcnt = 0, 0
#             ncnt = dfs4(n, n)
#             if n.left:
#                 lcnt = dfs3(n.left)
#             if n.right:
#                 rcnt = dfs3(n.right)
#             return ncnt + lcnt + rcnt
#
#         dfs1(root)
#         dfs2(root)
#         return dfs3(root) + dfs4(root,TreeNode(0))
from collections import defaultdict

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        sumdic = defaultdict(int)
        def dfs(n, sumv):
            if not n:
                return 0
            sumv += n.val
            res = sumdic.get(sumv-targetSum,0)
            sumdic[sumv] += 1
            res += dfs(n.left,sumv)
            res += dfs(n.right,sumv)
            sumdic[sumv] -= 1
            return res
        sumdic[0] = 1
        return dfs(root,0)


if __name__ == '__main__':
    s = Solution()
    c = Codec()
    root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root, t = [5,4,8,11,None,13,4,7,2,None,None,5,1], 22
    # root, t = [0,1,1], 0
    root = c.deserialize2(root)
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.pathSum(root, t)
    print(r)
