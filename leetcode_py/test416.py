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
    def canPartition(self, nums: List[int]) -> bool:
        maxn = max(nums)
        n = len(nums)
        sumn = sum(nums)
        if sumn % 2 == 1 or maxn > sumn // 2:
            return False
        h = sumn // 2
        # i 数组0:i j 价值0:j
        # A = [[False for _ in range(0,h+1)] for _ in range(0, n)]
        A = [False for _ in range(0,h+1)]
        A[0] = True
        A[nums[0]] = True
        for i in range(1,n):
            for j in range(h, -1,-1):
                if j < nums[i]:
                    A[j] = A[j]
                else:
                    A[j] = A[j] or A[j-nums[i]]
        return A[-1]


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
    r = s.canPartition([3,3,3,4,5])
    # 174801674
    print(r)
