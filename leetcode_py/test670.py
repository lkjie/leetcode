from collections import Counter, defaultdict
import copy
from typing import List
from leetcode_py.test297 import Codec
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from functools import reduce
from collections import Counter

# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         if num < 10:
#             return num
#         snum = list(str(num))
#         maxv = max(snum)
#         maxloc = len(snum) - 1 - snum[::-1].index(maxv)
#         if snum[0] == maxv:
#             padzero = 0
#             for i in range(1, len(snum)-1):
#                 if snum[i] == '0':
#                     padzero += 1
#                 else:
#                     break
#             remainnum = int("".join(snum[1:]))
#             return int(snum[0]+'0'*padzero + str(self.maximumSwap(remainnum)))
#         else:
#             snum[0], snum[maxloc] = snum[maxloc], snum[0]
#             return int("".join(snum))

from collections import defaultdict
if __name__ == '__main__':
    s = Solution()
    # c = Codec()
    # root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root = c.deserialize2(root)
    l = 99901
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.maximumSwap(l)
    print(r)
