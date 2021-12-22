import math

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        # 先排序
        nums = sorted(nums)
        # r保持最近接近的数，r_set保存abc的值
        res = nums[0] + nums[1] + nums[2]
        for i, a in enumerate(nums):
            # i, j, k分别表示abc当前位置指针
            j = i + 1
            k = len(nums) - 1
            while i < j < k:
                res_curr = nums[i] + nums[j] + nums[k]
                if res_curr - target == 0:
                    return res_curr
                # 两者挨在一起了，只判断一组数据
                if abs(res_curr - target) < abs(res - target):
                    res = res_curr
                if res_curr < target:
                    j = j + 1
                else:
                    k = k - 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10], -52))