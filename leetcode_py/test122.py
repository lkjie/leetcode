from typing import List
from collections import Counter, defaultdict
import copy


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        keepA = [0 for _ in prices]
        saleA = [0 for _ in prices]
        keepA[0] = -prices[0]
        for i in range(1, len(prices)):
            keepA[i] = max(keepA[i-1], saleA[i-1]-prices[i])
            saleA[i] = max(saleA[i-1], keepA[i-1]+prices[i])
        return saleA[-1]


if __name__ == '__main__':
    s = Solution()
    l = [7,1,5,3,6,4]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.maxProfit(l)
    # 174801674
    print(r)
