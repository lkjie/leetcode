# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lefts = []
        self.rights = []

    def addNum(self, num: int) -> None:
        if len(self.lefts) == 0:
            heapq.heappush(self.lefts,-num)
        elif num <= -self.lefts[0]:
            heapq.heappush(self.lefts, -num)
        else:
            heapq.heappush(self.rights, num)
        while len(self.lefts) - len(self.rights) >= 2:
            ni = heapq.heappop(self.lefts) * -1
            heapq.heappush(self.rights, ni)
        while len(self.rights) - len(self.lefts) >= 1:
            ni = heapq.heappop(self.rights)
            heapq.heappush(self.lefts, -ni)

    def findMedian(self) -> float:
        if len(self.lefts) > len(self.rights):
            return -self.lefts[0]
        else:
            return (-self.lefts[0] + self.rights[0]) * 1.0 / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


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
