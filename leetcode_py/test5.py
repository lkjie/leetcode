from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s
        A = [[False for _ in range(0, len(s))] for _ in range(0, len(s))]
        # for i in range(0, len(s)):
        #     A[i][i] = True
        resi, resj = 0, 0
        # for i in range(0, len(s)):
        #     for d in range(1,len(s)):
        #         j = i+d
        #         if s[i] == s[j] and A[i+1][j-1]:
        #             A[i][j] = True
        #             if d > resj - resi:
        #                 resi, resj = i, j
        return s[resi][resj]

if __name__ == '__main__':
    s = Solution()
    p = (
        [1, 3, 5, 8, 9, 11],
        [2, 4, 7, 10, 12, 13]
    )
    p = (
        [1,],
        []
    )
    r = s.findMedianSortedArrays(*p)
    print(r)