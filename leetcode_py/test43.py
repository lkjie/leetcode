from typing import List
from collections import Counter

def bigadd(str1, str2):
    if str1 == '0':
        return str2
    if str2 == '0':
        return str1
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    len1 = len(str1)
    len2 = len(str2)
    res = ''
    inc = 0
    str1 = str1[::-1]
    str2 = str2[::-1]
    for i in range(0, len2):
        if i < len1:
            resi = int(str1[i]) + int(str2[i]) + inc
        else:
            resi = int(str2[i]) + inc
        inc = resi // 10
        resi = resi % 10
        res = str(resi) + res
    if inc:
        res = str(inc) + res
    return res

def multiply_one(str1, a):
    assert 0 <= a <= 9
    if a == 0:
        return str1
    if str1 == '0':
        return 0
    res = ""
    inc = 0
    for i in range(len(str1)-1,-1,-1):
        resi = int(str1[i]) * a + inc
        inc = resi // 10
        resi = resi % 10
        res = str(resi) + res
    if inc:
        res = str(inc) + res
    return res


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        stack = []
        for i in range(0, len(height)):
            while stack and height[i] >= stack[-1][0]:
                theight,idx = stack.pop(-1)
                if not stack:
                    break
                d = i-stack[-1][1]-1
                h = min(stack[-1][0], height[i]) - theight
                res += d*h
            stack.append((height[i],i))
        return res


if __name__ == '__main__':
    s = Solution()
    r = bigadd('12323543214','12323543214')
    r = multiply_one('12323543214',5)
    # 174801674
    print(r)
