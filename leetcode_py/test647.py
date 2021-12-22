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
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        # 奇数
        n = len(s)
        res = 0
        for midloc in range(0, n):
            res += 1
            pl, pr = midloc - 1, midloc + 1
            while pl >= 0 and pr <= n - 1:
                if s[pl] == s[pr]:
                    res += 1
                    pl -= 1
                    pr += 1
                else:
                    break
        # 偶数
        for midloc in range(0, n):
            if midloc + 1 > n - 1:
                break
            if s[midloc] != s[midloc + 1]:
                continue
            res += 1
            pl, pr = midloc - 1, midloc + 2
            while pl >= 0 and pr <= n - 1:
                if s[pl] == s[pr]:
                    res += 1
                    pl -= 1
                    pr += 1
                else:
                    break
        return res


from collections import defaultdict
if __name__ == '__main__':
    s = Solution()
    # c = Codec()
    # root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root = c.deserialize2(root)
    l = 'aaa'
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.countSubstrings(l)
    print(r)
