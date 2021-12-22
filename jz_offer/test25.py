# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        dummy_h = RandomListNode(None)
        dummy_h.next = pHead

        ph = dummy_h
        dummy_h_new = RandomListNode(None)
        ph_new = dummy_h_new
        rand_dic = {}
        while ph.next:
            pn = ph.next
            p1 = RandomListNode(pn.label)
            ph_new.next = p1
            rand_dic[pn] = p1
            ph = pn
            ph_new = p1
        ph_new = dummy_h_new.next
        ph = dummy_h.next
        while ph_new:
            ph_new.random = rand_dic[ph.random]
            ph_new = ph_new.next
            ph = ph.next
        return dummy_h_new.next


if __name__ == '__main__':
    p1 = RandomListNode(1)
    p2 = RandomListNode(21)
    p3 = RandomListNode(3)
    p4 = RandomListNode(4)
    p5 = RandomListNode(5)
    p6 = RandomListNode(6)
    p1.next = p2
    p1.random = p4
    p2.next = p3
    p2.random = p1
    p3.next = p4
    p3.random = p4
    p4.next = p5
    p4.random = p4
    p5.next = p6
    s = Solution()
    s.Clone(p1)
