
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter, defaultdict
from typing import List

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        A = [0 for _ in nums]
        resall = 0
        A[0] = 1
        for i in range(1, len(nums)):
            res = 1
            for j in range(0,i):
                if nums[j] < nums[i]:
                    res = max(res, A[j]+1)
            A[i] = res
            resall = max(res, resall)
        return resall


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    s = Solution()
    t = [1,2,3,'null','null',4,5]
    t = map(str,t)
    r = s.lengthOfLIS([1,3,6,7,9,4,10,5,6])
    print(r)
