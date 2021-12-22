from typing import List
from collections import Counter, defaultdict
import copy

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, h = 0, n-1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < nums[0]:
                h = mid
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                if nums[l] < nums[h]:
                    h -= 1
                else:
                    l += 1
        return nums[l]
        # if h==n-1:
        #     return min(nums[l:h])
        # else:
        #     return min(nums[l:h+1])


if __name__ == '__main__':
    s = Solution()
    l = [11,13,15,17]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.findMin(l)
    # 174801674
    print(r)
