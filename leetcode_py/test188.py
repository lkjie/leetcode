from typing import List
from collections import Counter, defaultdict
import copy


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        b = [-prices[0] for _ in range(0, k)]
        s = [0 for _ in range(0, k)]
        for i in range(1, len(prices)):
            for j in range(0, k):
                if j == 0:
                    b[j] = max(b[j], -prices[i])
                else:
                    b[j] = max(b[j], s[i-1]-prices[i])
                s[j] = max(s[j], b[j]+prices[i])
        return max(s)


if __name__ == '__main__':
    s = Solution()
    l = [3,2,6,5,0,3]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.maxProfit(2, l)
    # 174801674
    print(r)
