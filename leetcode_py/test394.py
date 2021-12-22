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
    def decodeString(self, s: str) -> str:
        if not s or '[' not in s:
            return s
        # find k
        i = 0
        while s[i] < '0' or s[i] > '9':
            i += 1
        k_s = i
        while s[i] != '[':
            i += 1
        k_e = i
        k = int(s[k_s:k_e])
        # find [*]
        stack = []
        bracket_cnt = 1
        i += 1
        while  not (s[i] == ']' and bracket_cnt == 1):
            if s[i] == '[':
                bracket_cnt += 1
            elif s[i] == ']':
                bracket_cnt -= 1
            stack.append(s[i])
            i += 1
        i += 1
        bracket_str = self.decodeString(''.join(stack))
        decodestr = s[:k_s] + bracket_str * k + s[i:]
        decodestr = self.decodeString(decodestr)
        return decodestr


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
    r = s.decodeString("3[a]2[bc]")
    # 174801674
    print(r)
