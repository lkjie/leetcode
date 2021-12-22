# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        def trans(pRootOfTree):
            if not pRootOfTree:
                return None, None
            lp, lr = None, None
            lp1, lp2 = trans(pRootOfTree.left)
            lr1, lr2 = trans(pRootOfTree.right)
            if lp1:
                if lp1 == lp2:
                    lp1.right = pRootOfTree
                pRootOfTree.left = lp2
                lp = lp1
            else:
                lp = pRootOfTree
                pRootOfTree.left = None
            if lr1:
                if lr1 == lr2:
                    lr1.left = pRootOfTree
                pRootOfTree.right = lr1
                lr = lr2
            else:
                lr = pRootOfTree
                pRootOfTree.right = None
            return lp, lr
        lp, lr = trans(pRootOfTree)
        return lp


if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(21)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    # p5 = TreeNode(5)
    # p6 = TreeNode(6)
    p1.left = None
    p1.right = None
    p2.left = None
    p2.right = None
    p3.left = p1
    p3.right = p4
    p4.left = None
    p4.right = p2
    s = Solution()
    s.Convert(p3)
