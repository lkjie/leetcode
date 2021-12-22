from typing import List
from collections import Counter, defaultdict
import copy

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        assert len(s) > 0
        assert len(wordDict) > 0
        wset = set(wordDict)
        A = [False for i in range(0,len(wordDict))]
        for i in range(0,len(wordDict)):
            flag = s[0:i+1] in wset
            for j in range(1,i+1):
                flag = flag or (A[j-1] and s[j:i+1] in wset)
            A[i] = flag
        return A[-1]


if __name__ == '__main__':
    s = Solution()
    l = [7,1,5,3,6,4]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.wordBreak("leetcode",
["leet","code"])
    # 174801674
    print(r)
