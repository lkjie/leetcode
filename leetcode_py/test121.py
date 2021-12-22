from typing import List
from collections import Counter, defaultdict
import copy


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # st = []
        # res = 0
        # maxright = [-1 for i in range(0, len(prices))]
        # for i in range(len(prices)-1,-1,-1):
        #     while st and st[-1][0] <= prices[i]:
        #         st.pop(-1)
        #     if st:
        #         maxright[i] = st[0][0]
        #     st.append((prices[i],i))
        # for i in range(0, len(prices)):
        #     if maxright[i] != -1:
        #         res = max(res, maxright[i]-prices[i])
        # return res
        A = [[0,0] for i in range(0,len(prices))]
        A[0][0] = 0
        A[0][1] = -prices[0]
        for i in range(1, len(prices)):
            A[i][0] = max(A[i-1][0], A[i-1][1]+prices[i])
            A[i][1] = max(A[i-1][1], -prices[i])
        return A[-1][0]


if __name__ == '__main__':
    s = Solution()
    l = [7,1,5,3,6,4]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.maxProfit(l)
    # 174801674
    print(r)
