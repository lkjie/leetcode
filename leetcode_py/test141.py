from typing import List
from collections import Counter, defaultdict
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p1 = head
        p2 = head.next
        while p1 != p2 and p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
            if p1 == None or p2 == None:
                return False
            if p1 == p2:
                return True
            p2 = p2.next
            if p1 == p2:
                return True
        if p1 == None or p2 == None:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    l = ListNode(1)
    # l = [7,1,5,3,6,4]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.hasCycle(l)
    # 174801674
    print(r)
