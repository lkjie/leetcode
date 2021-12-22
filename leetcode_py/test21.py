
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
import heapq


class Solution:
    def mergeKLists(self, lists):
        head = ListNode(0)
        res = head
        heap_list = []
        list_cnt = len(lists)
        for i in range(0, len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap_list, (lists[i].val, i))
                if lists[i].next:
                    lists[i] = lists[i].next
                else:
                    lists[i] = None
                    list_cnt -= 1
            else:
                list_cnt -= 1
        while list_cnt>0:
            val, i = heapq.heappop(heap_list)
            node = ListNode(val)
            res.next = node
            res = node
            if lists[i] is not None:
                heapq.heappush(heap_list, (lists[i].val, i))
                if lists[i].next:
                    lists[i] = lists[i].next
                else:
                    lists[i] = None
                    list_cnt -= 1
        for i in range(len(heap_list)):
            node = ListNode(heapq.heappop(heap_list)[0])
            res.next = node
            res = node
        return head.next


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
    l1 = buildNode([1,4,5])
    l2 = buildNode([1,3,4])
    l3 = buildNode([2,6])
    print(s.mergeKLists([l1, l2, l3]))