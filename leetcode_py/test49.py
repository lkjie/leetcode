from typing import List
from collections import Counter, defaultdict
import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        assert len(matrix) == len(matrix[0])
        n = len(matrix)
        for j in range(0,n//2):
            rowleft, rowright = j, n - 1 - j
            for i in range(0, rowright-rowleft):
                a,b,c,d = matrix[rowleft][rowleft+i], matrix[rowleft+i][rowright], matrix[rowright][rowright-i], matrix[rowright-i][rowleft]
                matrix[rowleft][rowleft + i], matrix[rowleft + i][rowright], matrix[rowright][rowright - i], \
                matrix[rowright - i][rowleft] = d,a,b,c
            rowleft+=1
            rowright-=1


if __name__ == '__main__':
    s = Solution()
    l = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.rotate(l)
    # 174801674
    print(l)
