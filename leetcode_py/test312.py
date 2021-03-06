
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter, defaultdict
from typing import List
from heapq import heappush, heappop, heapify
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import heapq

# 错的，为啥错了还没整明白
# [21,97,60,1] 得先戳90
# class Solution:
    # def maxCoins(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     h = []
    #     for i, n in enumerate(nums):
    #         if i > 0 and i < len(nums) - 1:
    #             heappush(h, (n,i))
    #     res = 0
    #     mask = [False for _ in range(0, len(nums))]
    #     while h:
    #         ni, idx = heappop(h)
    #         lastidx = idx - 1
    #         while mask[lastidx]:
    #             lastidx -= 1
    #         nextidx = idx + 1
    #         while mask[nextidx]:
    #             nextidx += 1
    #         res += nums[lastidx] * nums[idx] * nums[nextidx]
    #         mask[idx] = True
    #     res += nums[0] * nums[-1] + max(nums[0], nums[-1])
    #     return res


# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         res = 0
#         if not nums:
#             return res
#         val = [1] + nums + [1]
#         @lru_cache(None)
#         def solve(i,j):
#             if i >= j - 1:
#                 return 0
#             max_val = 0
#             for mid in range(i+1,j):
#                 ri = val[i] * val[mid] * val[j] + solve(i,mid) + solve(mid, j)
#                 max_val = max(ri, max_val)
#             return max_val
#         return solve(0, len(val)-1)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        res = 0
        if not nums:
            return res
        val = [1] + nums + [1]
        A = [[0 for _ in val] for _ in val]
        n = len(val)
        for i in range(n,-1,-1):
            for j in range(i+1, n):
                for mid in range(i+1,j):
                    ri = val[i] * val[mid] * val[j] + A[i][mid] + A[mid][j]
                    A[i][j] = max(A[i][j], ri)
        return A[0][-1]


if __name__ == '__main__':
    s = Solution()
    l = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    # l = [3,1,5,8]
    r = s.maxCoins(l)
    print(r)
