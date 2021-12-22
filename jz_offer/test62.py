# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.i = 0
        self.res = None
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        def mid_search(node):
            if not node:
                return
            if self.res:
                return
            mid_search(node.left)
            self.i += 1
            if self.i ==k:
                self.res = node.val
                return
            mid_search(node.right)
        mid_search(pRoot)
        return self.res

if __name__ == '__main__':
    p1 = TreeNode(5)
    p2 = TreeNode(2)
    p3 = TreeNode(1)
    p4 = TreeNode(7)
    p5 = TreeNode(4)
    p1.left = p2
    p1.right = p4
    p2.left = p3
    p2.right = None
    p3.left = None
    p3.right = None
    p4.left = None
    p4.right = None
    s = Solution()
    res = s.KthNode(p1,1)
    print(res)
