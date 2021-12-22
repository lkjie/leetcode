from typing import List
from collections import Counter, defaultdict
import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math
from functools import cmp_to_key


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(x[0],-x[1]))
        def getnextloc(res, idx):
            while res[idx]!= None:
                idx += 1
            return idx
        res = [[] for _ in people]
        for h,k in people:
            idx = getnextloc(res, 0)
            ki = k
            while k != 0:
                idx = getnextloc(res, idx+1)
                k -= 1
            res[idx] = [h,ki]
        return res


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
    r = s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    # 174801674
    print(r)
