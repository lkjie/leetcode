
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(next=head)
        p_last = dummy_head
        p_s = dummy_head.next
        p_e = p_s
        for i in range(0, k-1):
            p_e = p_e.next if p_e else None
        while p_s and p_e:
            p_last.next = p_e
            p1 = p_s
            p2 = p1.next
            p1.next = p_e.next
            for i in range(0, k-1):
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
            p_last = p_s
            p_s = p_s.next
            p_e = p_s
            for i in range(0, k-1):
                p_e = p_e.next if p_e else None
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
    l1 = buildNode([1,2,3,4,5])
    print(s.reverseKGroup(l1, 2))