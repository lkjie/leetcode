from typing import List
from collections import Counter

# ac1
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         n = len(nums)
#         if n <= 2:
#             if target not in nums:
#                 return -1
#             return nums.index(target)
#         if nums[0] > nums[-1]:
#             #旋转过，确定边界
#             pl, ph = 0, n-1
#             while pl <= ph:
#                 if nums[pl] < nums[ph]:
#                     break
#                 elif nums[pl] == nums[ph]:
#                     break
#                 elif nums[pl] > nums[ph]:
#                     mid = (pl + ph) // 2
#                     if nums[mid] < nums[pl]:
#                         ph = mid
#                     elif nums[mid] == nums[pl]:
#                         break
#                     elif nums[mid] > nums[pl]:
#                         pl = mid + 1
#             low = pl if nums[pl] < nums[ph] else ph
#             if target >= nums[0] and target <= nums[low-1]:
#                 pl,ph = 0, low
#             else:
#                 pl,ph = low,n
#         else:
#             pl,ph = 0, n
#         while pl < ph:
#             mid = (pl + ph) // 2
#             if nums[mid] > target:
#                 ph = mid
#             elif nums[mid] == target:
#                 return mid
#             else:
#                 pl = mid + 1
#         return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        l,h = 0, n-1
        while l <= h:
            mid = (l+h)//2
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[n-1]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    l = [1,3], 3
    r = s.search(*l)
    print(r)
