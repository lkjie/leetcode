from typing import List
from collections import Counter, defaultdict
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        def dfs(vds,paths,depth,res):
            if depth == len(nums):
                res.append(copy.deepcopy(paths))
            else:
                paths.append(nums[depth])
                dfs(vds,paths,depth+1,res)
                paths.remove(nums[depth])
                dfs(vds,paths,depth+1,res)
        res = []
        vds = [False for _ in range(0, len(nums))]
        dfs(vds,[],0,res)
        return res


if __name__ == '__main__':
    s = Solution()
    l = [0,0,1,0,1,1,2,2]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.subsets([1,2,3,4,5,6,7,8,10,0])
    # 174801674
    print(r)
