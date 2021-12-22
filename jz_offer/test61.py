# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        def firsts(node):
            if not node:
                return '#!'
            res = "{}!".format(node.val)
            return res + firsts(node.left) + firsts(node.right)
        return firsts(root)
    def Deserialize(self, s):
        # write code here
        s = s.split('!')
        s = list(filter(lambda x:x != '', s))
        def build():
            if s[0] == '#':
                return None
            p = TreeNode(int(s[0]))
            s.pop(0)
            p.left = build()
            p.right = build()
            return p
        return build()

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
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
    res = s.Serialize(p1)
    r = s.Deserialize(res)
