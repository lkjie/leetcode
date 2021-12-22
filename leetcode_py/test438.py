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

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c1 = Counter(p)
        plen = len(p)
        res = []
        c2 = Counter(s[0:plen - 1])
        for i in range(0, len(s) - plen + 1):
            c2[s[i + plen - 1]] += 1
            if c1 == c2:
                res.append(i)
            c2[s[i]] -= 1
            if c2[s[i]] == 0:
                c2.pop(s[i])
        return res


if __name__ == '__main__':
    s = Solution()
    c = Codec()
    root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root, t = [5,4,8,11,None,13,4,7,2,None,None,5,1], 22
    # root, t = [0,1,1], 0
    root = c.deserialize2(root)
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.findAnagrams("cbaebabacd",
"abc")
    print(r)
