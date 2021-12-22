from typing import List
from collections import Counter, defaultdict
import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        p1 = 0
        p2 = 0
        if not t or not s:
            return ""
        res = None
        cs = Counter(s[0])
        ct = Counter(t)
        while p1 < len(s) and p2 < len(s):
            if not ct - cs:
                if res is None or p2-p1+1 < len(res):
                    res = s[p1:p2+1]
                cs[s[p1]] -= 1
                p1 += 1
            else:
                p2 += 1
                if p2 < len(s):
                    cs.update(s[p2])
        return "" if res is None else res

if __name__ == '__main__':
    s = Solution()
    l = [0,0,1,0,1,1,2,2]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.minWindow(
"ADOBECODEBANC",
"ABC")
    # 174801674
    print(r)
