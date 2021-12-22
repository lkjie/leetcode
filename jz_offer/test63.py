# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.win = []
#         self.nl = 0
#         self.nr = 0
#         self.win_len = 100
#     def Insert(self, num):
#         # write code here
#         if not self.win:
#             self.win.append(num)
#             return
#         pl = 0
#         ph = len(self.win) - 1
#         while pl <= ph:
#             pm = (pl + ph)//2
#             if num < self.win[pm]:
#                 ph = pm - 1
#             elif num == self.win[pm]:
#                 pl = pm
#                 ph = pm
#                 break
#             else:
#                 pl = pm + 1
#         self.win.insert(pl, num)
#         if len(self.win) > self.win_len:
#             if self.nl < self.nr:
#                 self.win.pop(1)
#                 self.nl += 1
#             else:
#                 self.win.pop(-1)
#                 self.nr += 1
#     def GetMedian(self):
#         # write code here
#         n = self.nl + self.nr + len(self.win)
#         if n % 2 == 1:
#             return self.win[n//2 - self.nl]
#         else:
#             return (self.win[n//2 - self.nl] + self.win[n//2 - self.nl - 1])/2


# 解法2
# import heapq
# class Solution:
#     def __init__(self):
#         self.heapl = []
#         self.heapr = []
#     def Insert(self, num):
#         # write code here
#         heapq.heappush(self.heapl, num*-1)
#         while len(self.heapl) > len(self.heapr):
#             r1 = heapq.heappop(self.heapl)*-1
#             heapq.heappush(self.heapr, r1)
#         if len(self.heapl) == 0 and len(self.heapr) == 1:
#             return
#         while  self.heapl[0]*-1 > self.heapr[0]:
#             rl = heapq.heappop(self.heapl)*-1
#             rr = heapq.heappop(self.heapr)
#             heapq.heappush(self.heapr, rl)
#             heapq.heappush(self.heapr, rr*-1)
#     def GetMedian(self):
#         # write code here
#         if len(self.heapl) == len(self.heapr):
#             return (self.heapr[0] + self.heapl[0]*-1)/2
#         else:
#             return self.heapr[0]

from heapq import heappop, heappush
class Solution:
    def __init__(self):
        self.A = []#小顶堆，存储较大的一半
        self.B = []#大顶堆，存储较小的一半
    def Insert(self, num):
        # write code here
        if len(self.A) == len(self.B):#当A,B元素个数相等时，向A添加元素
            heappush(self.B,-num)
            heappush(self.A,-heappop(self.B))
        else:#当A,B元素个数不等时，向B添加元素
            heappush(self.A,num)
            heappush(self.B,-heappop(self.A))
    def GetMedian(self):
        # write code here
        if len(self.A) == len(self.B):
            return (self.A[0]-self.B[0])/2.0#注意B里存的是相反数，这里写2.0可以让输出结果保留小数位
        else:
            return self.A[0]


if __name__ == '__main__':
    s = Solution()
    s.Insert(1)
    print(s.GetMedian())
    s.Insert(2)
    print(s.GetMedian())
    s.Insert(3)
    print(s.GetMedian())
    s.Insert(4)
    print(s.GetMedian())
    s.Insert(5)
    print(s.GetMedian())
