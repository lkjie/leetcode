import math

class Solution:
    def fourSum(self, nums, target: int):
        nums = sorted(nums)
        res = set()
        for a in range(0, len(nums)-3):
            for b in range(a+1 , len(nums)-2):
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
                        c = c + 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c = c + 1
                    else:
                        d = d - 1
        res = list(map(list, res))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))