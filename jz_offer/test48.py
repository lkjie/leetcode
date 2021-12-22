# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Add(self, num1, num2):
        # write code here
        mx = 0xffffffffffffffff
        num1 &= mx
        num2 &= mx
        while num2:
            s = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = s & mx
        return num1 if num1 >> 63==0 else ~(num1^mx)


if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(21)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    # p5 = TreeNode(5)
    # p6 = TreeNode(6)
    s = Solution()
    r = s.Add(-1,-100)
    print(r)
