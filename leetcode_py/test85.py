from typing import List
from collections import Counter, defaultdict
import copy

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rowl, coll = len(matrix), len(matrix[0])
        if rowl == 0 or coll == 0:
            return 0
        Aleft = [[0 for i in range(0, coll)] for _ in range(0, rowl)]
        for ri in range(0, rowl):
            left1cnt = 0
            for cj in range(0, coll):
                if matrix[ri][cj] == '1':
                    left1cnt += 1
                else:
                    left1cnt = 0
                Aleft[ri][cj] = left1cnt
        def getmaxsize(arr):
            st = []
            res = 0
            leftls = [-1 for i in range(0, len(arr))]
            rightls = [-1 for i in range(0,len(arr))]
            for i in range(0, len(arr)):
                while st and st[-1][0] >= arr[i]:
                    rightls[st[-1][1]] = i
                    st.pop(-1)
                if not st:
                    leftls[i] = -1
                else:
                    leftls[i] = st[-1][1]
                st.append((arr[i],i))
            for i in range(0, len(arr)):
                r = rightls[i] if rightls[i] != -1 else len(arr)
                res = max(res, (r - leftls[i] - 1)*arr[i])
            return res
        res = 0
        for i in range(0, coll):
            arr = [Aleft[j][i] for j in range(0, rowl)]
            res = max(res, getmaxsize(arr))
        return res


if __name__ == '__main__':
    s = Solution()
    l = [["1"]]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.maximalRectangle(l)
    # 174801674
    print(r)
