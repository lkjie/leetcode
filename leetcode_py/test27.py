
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


def buildNode(l):
    h = ListNode()
    last = h
    for i in l:
        n = ListNode(i)
        last.next = n
        last = n
    return h.next


class Solution:
    def removeElement(self, nums, val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2 + 1:
            if nums[p1] == val:
                nums[p1] = nums[p2]
                p2 -= 1
            else:
                p1 += 1
        return p2 + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,3], 3))