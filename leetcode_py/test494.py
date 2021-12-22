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

class Solution:
    # def __init__(self):
    #     self.res = 0

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     def dfs(idx,pathsum):
    #         if idx == n:
    #             if pathsum == target:
    #                 self.res+=1
    #             return
    #         dfs(idx+1,pathsum+nums[idx])
    #         dfs(idx+1,pathsum-nums[idx])
    #     dfs(0,0)
    #     return self.res
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        sumN = sum(nums)
        A = [0 for _ in range(0, sumN*2+1)]
        A[nums[0]+sumN] = 1
        A[-nums[0]+sumN] = 1
        for i in range(1,n):
            A1 = A.copy()
            for j in range(-sumN,sumN+1):
                if j-nums[i]+sumN < 0:
                    A1[j+sumN] = A[j+nums[i]+sumN]
                elif j+nums[i]+sumN > 2*sumN:
                    A1[j+sumN] = A[j-nums[i]+sumN]
                else:
                    A1[j+sumN] = A[j-nums[i]+sumN] + A[j+nums[i]+sumN]
            A = A1
        if target + sumN < 0 or target + sumN > 2*sumN:
            return 0
        return A[target + sumN]

if __name__ == '__main__':
    s = Solution()
    c = Codec()
    root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root, t = [5,4,8,11,None,13,4,7,2,None,None,5,1], 22
    # root, t = [0,1,1], 0
    l = [0,0,0,0,0,0,0,0,1], 1
    root = c.deserialize2(root)
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.findTargetSumWays(*l)
    print(r)
    [].count()
