
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        last_n = dummy_head
        if head is None or head.next is None:
            return head
        n1 = head
        n2 = n1.next
        while n1 and n2:
            n3 = n2.next
            last_n.next = n2
            n1.next = n3
            n2.next = n1
            last_n = n1
            n1 = n3
            n2 = n1.next if n1 else None
        return dummy_head.next


def buildNode(l):
    h = ListNode()
    last = h
    for i in l:
        n = ListNode(i)
        last.next = n
        last = n
    return h.next


if __name__ == '__main__':
    s = Solution()
    l1 = buildNode([1,2,3,4])
    print(s.swapPairs(l1))