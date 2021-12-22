from typing import List
from collections import Counter, defaultdict
import copy

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # 按列搜索
        # res = [0 for i in range(0,len(heights))]
        # res = heights[0]
        # for pleft in range(0,len(heights)):
        #     h = heights[pleft]
        #     for pright in range(pleft,len(heights)):
        #         hi = heights[pright]
        #         h = min(h,hi)
        #         res = max(res, h*(pright-pleft+1))
        # return res
        # 按高搜索
        # res = heights[0]
        # h = max(heights)
        # for hi in range(1, h+1):
        #     pleft = 0
        #     for i in range(0, len(heights)):
        #         if heights[i] < hi:
        #             if i < len(heights)-1:
        #                 pleft = i+1
        #         else:
        #             res = max(res, hi*(i-pleft+1))
        # return res
        # 单调栈
        stleft = []
        stright = []
        leftlocs = [-1 for i in range(0, len(heights))]
        rightlocs = [-1 for i in range(0, len(heights))]
        # def buildlocs(stleft, leftlocs, rgs):
        #     for i in rgs:
        #         while stleft and stleft[-1][0] >= heights[i]:
        #             stleft.pop(-1)
        #         if not stleft:
        #             leftlocs.append(-1)
        #         else:
        #             leftlocs.append(stleft[-1][1])
        #         stleft.append((heights[i],i))
        # buildlocs(stleft, leftlocs, range(0, len(heights)))
        # buildlocs(stright, rightlocs, range(len(heights)-1,-1,-1))
        for i in range(0, len(heights)):
            while stleft and stleft[-1][0] >= heights[i]:
                rightlocs[stleft[-1][1]] = i
                stleft.pop(-1)
            if not stleft:
                leftlocs[i]=-1
            else:
                leftlocs[i]=stleft[-1][1]
            stleft.append((heights[i],i))
        # rightlocs = rightlocs[::-1]
        res = heights[0]
        for i in range(0, len(heights)):
            pl,pr = leftlocs[i], rightlocs[i]
            if pr == -1:
                pr = len(heights)
            res = max(res, (pr-pl-1)*heights[i])
        return res


if __name__ == '__main__':
    s = Solution()
    l = [1,1]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.largestRectangleArea(l)
    # 174801674
    print(r)
