from typing import List
from collections import Counter, defaultdict
import copy

from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # c = Counter(nums)
        # n0,n1,n2 = c.get(0,0), c.get(1,0),c.get(2,0)
        # for i in range(0, len(nums)):
        #     if n0:
        #         nums[i] = 0
        #         n0-=1
        #     elif n1:
        #         nums[i] = 1
        #         n1-=1
        #     else:
        #         nums[i] = 2
        # return nums
        p1 = 0
        p2 = len(nums)-1
        for i in range(0,p2+1):
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1



if __name__ == '__main__':
    s = Solution()
    l = [0,0,1,0,1,1,2,2]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.sortColors(l)
    # 174801674
    print(l)
