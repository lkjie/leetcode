# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 先判断是否有环
        p1 = pHead
        p2 = pHead.next
        is_loop = False
        while p2:
            n1 = p1.next
            n21 = p2.next
            n22 = n21.next if n21 else None
            p1 = n1
            p2 = n22
            if (n1 == n21 or n1 == n22) and n1 != None:
                is_loop = True
                break
        if not is_loop:
            return None
        # 测量环长度
        p10 = p1
        p1 = p1.next
        cnt = 1
        while p1 != p10:
            cnt += 1
            p1 = p1.next
        p1 = pHead
        p2 = pHead
        # 找头节点
        for _ in range(0, cnt):
            p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p3
    s = Solution()
    s.EntryNodeOfLoop(p3)
