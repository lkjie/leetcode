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
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 构建并查集
        s = {}
        s_v = {}

        def find(a):
            if s[a] == a:
                return a
            else:
                root = find(s[a])
                s_v[a] = s_v[s[a]] * s_v[a]
                s[a] = root
                return s[a]

        def merge(a, b, v):
            ra = find(a)
            rb = find(b)
            s[ra] = rb
            s_v[ra] = s_v[b] / s_v[a] * v

        for (a, b), v in zip(equations, values):
            s[a] = a
            s[b] = b
            s_v[a] = 1
            s_v[b] = 1
        for (a, b), v in zip(equations, values):
            merge(a, b, v)
        res = []
        for a, b in queries:
            if a not in s or b not in s:
                res.append(-1)
            else:
                ra = find(a)
                rb = find(b)
                if ra != rb:
                    res.append(-1)
                else:
                    res.append(s_v[a] / s_v[b])
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
    r = s.calcEquation([["a","b"],["e","f"],["b","e"]],
[3.4,1.4,2.3],
[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]])
    # 174801674
    print(r)

import math
import functools
functools.cmp_to_key()
