from typing import List
from collections import Counter, defaultdict
import copy


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        keep = [0 for _ in range(0, len(prices))]
        cold = [0 for _ in range(0, len(prices))]
        nop = [0 for _ in range(0, len(prices))]
        keep[0] = -prices[0]
        for i in range(1, len(prices)):
            keep[i] = max(keep[i-1], -prices[i])
            cold[i] = keep[i-1]+prices[i]
            nop[i] = max(nop[i-1], cold[i-1])
        return max(nop[-1], cold[-1])


if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,0,2]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.maxProfit( l)
    # 174801674
    print(r)
