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
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(0, n+1)]
        mask = 0xFFFF
        for i in range(1,n+1):
            maxidx = 1
            while (mask << maxidx) & i != 0:
                maxidx += 1
            res[i] = res[i - (0x1 << (maxidx-1))] + 1
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
    r = s.countBits(5)
    # 174801674
    print(r)
