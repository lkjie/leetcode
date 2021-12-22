# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) == 0:
            return matrix
        row = len(matrix[0])
        col = len(matrix)
        # 圈数
        i = 0
        res = []
        while 2*i < col and 2*i < row:
            end_row = row - i - 1
            end_col = col - i - 1
            for i1 in range(i, end_row + 1):
                res.append(matrix[i][i1])
            for i1 in range(i+1, end_col + 1):
                res.append(matrix[i1][end_row])
            if end_col > i:
                for i1 in range(end_row-1, i-1, -1):
                    res.append(matrix[end_col][i1])
            if end_row > i:
                for i1 in range(end_col-1, i, -1):
                    res.append(matrix[i1][i])
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    s.printMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])