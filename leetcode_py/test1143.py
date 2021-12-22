from collections import Counter, defaultdict
import copy
from typing import List
from leetcode_py.test297 import Codec
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from functools import reduce
from collections import Counter

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        t1len = len(text1)
        t2len = len(text2)
        res = 0
        A = [[0 for _ in range(0, t2len+1)] for _ in range(0, t1len+1)]
        # 1  i-- j--, 2 i--, 3 j--
        B = [[0 for _ in range(0, t2len+1)] for _ in range(0, t1len+1)]
        for i in range(0, len(text1)+1):
            for j in range(0, len(text2) + 1):
                if i == 0 or j == 0:
                    continue
                if text1[i-1] == text2[j-1]:
                    A[i][j] = A[i-1][j-1]+1
                    B[i][j] = 1
                elif text1[i-1] != text2[j-1]:
                    A[i][j] = 0
                    if A[i-1][j] > A[i][j-1]:
                        # A[i][j] = A[i-1][j]
                        B[i][j] = 2
                    else:
                        # A[i][j] = A[i][j-1]
                        B[i][j] = 3
                res = max(res, A[i][j])
        i,j = t1len,t2len
        res2 = ''
        restmp = ''
        while i > 0 and j > 0:
            if B[i][j] == 1:
                restmp = text1[i-1] + restmp
                i -= 1
                j -= 1
            elif B[i][j] == 2:
                i -= 1
                restmp = ''
            elif B[i][j] == 3:
                j -= 1
                restmp = ''
            else:
                break
            res2 = res2 if len(res2) > len(restmp) else restmp
        return res, res2


from collections import defaultdict
if __name__ == '__main__':
    s = Solution()
    # c = Codec()
    # root, t = [10,5,-3,3,2,None,11,3,-2,None,1], 8
    # root = c.deserialize2(root)
    l = 'aaa'
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.longestCommonSubsequence('abcde', 'abce')
    print(r)
    [].index()
