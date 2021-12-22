
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
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            p1 = i+1
            p2 = nums[i]
            if p1 != p2:
                if nums[p2-1] == p2:
                    return p1
                else:
                    nums[p2-1], nums[i] = nums[i], nums[p2-1]
            else:
                i += 1
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.findDuplicate( [3,1,3,4,2])
    print(r)
