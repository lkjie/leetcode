
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head
        last_p = p
        for i in range(0, n):
            q = q.next
        while q != None:
            q = q.next
            last_p = p
            p = p.next
        if p == head:
            return p.next
        last_p.next = p.next
        return head


if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,4,5]
    h = ListNode()
    last = h
    for i in l:
        n = ListNode(i)
        last.next = n
        last = n
    print(s.removeNthFromEnd(h, 2))