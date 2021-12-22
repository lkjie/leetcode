# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.res = 0
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         if k == 0:
#             return 1
#         def rowcolsum(r,c):
#             res = 0
#             while r > 0:
#                 res += r%10
#                 r = r // 10
#             while c > 0:
#                 res += c%10
#                 c = c // 10
#             return res
#         vised = [[False for _ in range(0,n)] for _ in range(0,m)]
#         def dfs(r,c,pathlen):
#             self.res = max(self.res, pathlen)
#             direction = [0,-1,0,1,0]
#             for i in range(0,4):
#                 ri = r + direction[i]
#                 ci = c + direction[i+1]
#                 if 0 <= ri <= m-1 and 0 <= ci <=n-1 and vised[ri][ci] == False:
#                     if rowcolsum(ri,ci) <= k:
#                         vised[ri][ci] = True
#                         dfs(ri,ci,pathlen+1)
#                         vised[ri][ci] = False
#         vised[0][0] = True
#         dfs(0,0,1)
#         return self.res


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        r = dfs(0, 0, 0, 0)
        return r


if __name__ == '__main__':
    s = Solution()
    r = s.movingCount(7,2,3)
    print(r)