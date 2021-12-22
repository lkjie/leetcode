from typing import List
from collections import Counter

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates = sorted(candidates)
        if target < candidates[0]:
            return []
        def greedy(candidates, target):
            if not candidates:
                return False
            if target < candidates[0]:
                return False
            if target == candidates[0]:
                return [[target]]
            res = []
            for i in range(0,len(candidates)):
                if target == candidates[i]:
                    res.append([target])
                elif target < candidates[i]:
                    break
                else:
                    resi = greedy(candidates[i:], target-candidates[i])
                    if resi:
                        for li in resi:
                            li.insert(0, candidates[i])
                        res+=resi
            return res
        return greedy(candidates, target)


if __name__ == '__main__':
    s = Solution()
    l = [1,3,2]
    r = s.combinationSum([2,3,6,7],
7)
    print(r)
