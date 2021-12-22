from typing import List
from collections import Counter
import copy

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return []
#         res = [[nums[0]]]
#         for i in range(1,len(nums)):
#             resnew = []
#             for j in range(0,len(res)):
#                 resj = res[j]
#                 for k in range(0,i+1):
#                     tmp = copy.deepcopy(resj)
#                     tmp.insert(k,nums[i])
#                     resnew.append(tmp)
#             res = resnew
#         return res


import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        def dfs(nums,nums_len,vds,depth,paths,reslst):
            if depth == nums_len:
                reslst.append(copy.deepcopy(paths))
            else:
                for i in range(0, nums_len):
                    if not vds[i]:
                        vds[i] = True
                        paths.append(nums[i])
                        dfs(nums,nums_len,vds,depth+1,paths,reslst)
                        paths.pop(-1)
                        vds[i]=False
        res = []
        vds = [False for i in range(0,len(nums))]
        dfs(nums,len(nums),vds,0,[],res)
        return res



if __name__ == '__main__':
    s = Solution()
    l = [1,2,3]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.permute(l)
    # 174801674
    print(r)
