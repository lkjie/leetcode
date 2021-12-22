from typing import List
from collections import Counter, defaultdict
import copy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        def mergesortedList(p1,p2):
            if not p1:
                return p2
            if not p2:
                return p1
            p3 = ListNode()
            pout = p3
            while p1 and p2:
                if p1.val < p2.val:
                    p3.next = p1
                    p1 = p1.next
                else:
                    p3.next = p2
                    p2 = p2.next
                p3 = p3.next
            if p1:
                p3.next = p1
            if p2:
                p3.next = p2
            return pout.next
        dummyhead = ListNode(next=head)
        d = 1
        n = 0
        p = head
        while p:
            p=p.next
            n+=1
        while d<n:
            pprev, pcurr = dummyhead, dummyhead.next
            while pcurr:
                phead1 = pcurr
                for i in range(1,d):
                    if pcurr.next:
                        pcurr = pcurr.next
                    else:
                        break
                phead2 = None
                if pcurr.next:
                    phead2 = pcurr.next
                    pcurr.next = None
                pcurr = phead2
                for i in range(1,d):
                    if pcurr.next:
                        pcurr = pcurr.next
                    else:
                        break
                pnext = None
                if pcurr.next:
                    pnext = pcurr.next
                    pcurr.next = None

                p1new = mergesortedList(phead1,phead2)
                pprev.next = p1new
                if pnext:
                    while p1new.next:
                        p1new = p1new.next
                    p1new.next = pnext
                pprev, pcurr = p1new, pnext
            d = d<<1
        return dummyhead.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    # l = [7,1,5,3,6,4]
    # l = [-1,5,3,4,0]
    # 174801674
