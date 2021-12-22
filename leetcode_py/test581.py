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

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return 0
        s = []
        idxl, idxr = len(nums)-1, 0
        maxleft = -1e10
        if nums[1] < nums[0]:
            idxl, idxr = 0, 1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                idxl = min(idxl, i-1)
                idxr = max(idxr, i)
                maxleft = max(maxleft, nums[i-1])
            elif nums[i-1] == nums[i] and nums[i] < maxleft:
                idxr += 1
        if idxr > idxl:
            return idxr - idxl + 1
        return 0
        # idxl, needfirst = 0, True
        # idxr = 0
        # for i in range(0, len(nums)):
        #     while s and nums[i] <= s[-1][0]:
        #         if needfirst:
        #             idxl = s[-1][1]
        #             needfirst = False
        #         idxr = i
        #         s.pop(-1)
        #     s.append((nums[i], i))
        # if idxr == 0:
        #     return 0
        # return idxr - idxl + 1


from collections import defaultdict
if __name__ == '__main__':
    s = Solution()
    c = Codec()
    root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root, t = [5,4,8,11,None,13,4,7,2,None,None,5,1], 22
    # root, t = [0,1,1], 0
    l = [2,3,3,2,4]
    c = Counter(l)
    root = c.deserialize2(root)
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.findUnsortedSubarray(l)
    print(r)
