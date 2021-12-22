
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        i = n-1 # 小数是i-1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                break
        if i == 1 and nums[0] >= nums[1]:
            return nums.reverse()
        for j in range(len(nums)-1,i-1,-1):
            if nums[j] > nums[i-1]:
                nums[j], nums[i-1] = nums[i-1], nums[j]
                break
        a = i if i!=0 else 0
        b = n-1
        while a<b:
            nums[a], nums[b] = nums[b], nums[a]
            a+=1
            b-=1


if __name__ == '__main__':
    s = Solution()
    l = [1,3,2]
    print(s.nextPermutation(l))
    print(l)