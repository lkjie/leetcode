# -*- coding:utf-8 -*-
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix char字符型二维数组
# @param word string字符串
# @return bool布尔型
#
class Solution:
    def hasPath(self , matrix , word ):
        # write code here
        if not matrix:
            return False
        if not word:
            return True
        nr, nc = len(matrix), len(matrix[0])
        vi = [[False for _ in range(nc)] for _ in range(nr)]
        def dfs(r,c,s,vi):
            if not s:
                return True
            if s[0] == matrix[r][c]:
                vi[r][c] = True
            else:
                return False
            if r > 0 and vi[r-1][c] == False:
                vi[r-1][c] = True
                dfs(r-1,c,s[1:],vi)
                vi[r-1][c] = False
            if c > 0 and vi[r][c-1] == False:
                vi[r][c-1] = True
                dfs(r,c-1,s[1:],vi)
                vi[r][c-1] = False
            if r < nr-1 and vi[r+1][c] == False:
                vi[r+1][c] = True
                dfs(r+1,c,s[1:],vi)
                vi[r+1][c] = False
            if c < nc - 1 and vi[r][c+1] == False:
                vi[r][c+1] = True
                dfs(r,c+1,s[1:],vi)
                vi[r][c+1] = False
            return False
        for i in range(0,nr):
            for j in range(0,nc):
                if dfs(i,j,word,vi):
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    s.hasPath([['a','b','c','e'],['s','f','c','s'],['a','d','e','e']],"see")
