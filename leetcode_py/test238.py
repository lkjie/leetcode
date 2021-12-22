
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter, defaultdict
from typing import List

from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        Aleft = [1 for _ in nums]
        Aright = [1 for _ in nums]
        for i in range(1, len(nums)):
            if i == 1:
                Aleft[i] = nums[i-1]
            else:
                Aleft[i] = Aleft[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            if i == len(nums)-2:
                Aright[i] = nums[i+1]
            else:
                Aright[i] = Aright[i+1] * nums[i+1]
        res = [0 for _ in nums]
        for i in range(0,len(nums)):
            res[i] = Aleft[i] * Aright[i]
        return res


if __name__ == '__main__':
    s = Solution()
    r = s.productExceptSelf([1,2,3,4])
    print(r)
