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
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        res = 0
        n = len(nums)
        if n == 1:
            if nums[0] != k:
                return 0
            else:
                return 1

        accnums = []
        acc = 0
        for i in nums:
            acc += i
            accnums.append(acc)
        acccnter = Counter(accnums)
        lsum = 0
        res += acccnter.get(k,0)
        for i in range(0, n):
            lsum += nums[i]
            for nj, cnt in acccnter.items():
                if nj - lsum == k:
                    res += cnt
        return res

from collections import defaul
if __name__ == '__main__':
    s = Solution()
    c = Codec()
    root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root, t = [5,4,8,11,None,13,4,7,2,None,None,5,1], 22
    # root, t = [0,1,1], 0
    l = [-1,-1,1], 0
    root = c.deserialize2(root)
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.subarraySum(*l)
    print(r)
