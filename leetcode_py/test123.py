from typing import List
from collections import Counter, defaultdict
import copy


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = [0 for _ in prices]
        s1 = [0 for _ in prices]
        b2 = [0 for _ in prices]
        s2 = [0 for _ in prices]
        b1[0] = -prices[0]
        b2[0] = -prices[0]
        for i in range(1, len(prices)):
            b1[i] = max(b1[i-1], -prices[i])
            s1[i] = max(s1[i-1], b1[i-1]+prices[i])
            b2[i] = max(b2[i-1], s1[i-1]-prices[i])
            s2[i] = max(s2[i-1], b2[i-1]+prices[i])
        return max(s1[i], s2[i])


if __name__ == '__main__':
    s = Solution()
    l = [3,3,5,0,0,3,1,4]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.maxProfit(l)
    # 174801674
    print(r)
