from typing import List
from collections import Counter, defaultdict
import copy


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        m, n = len(board), len(board[0])
        V = [[False for _ in range(0, n)] for _ in range(0, m)]
        direction = [0, -1, 0, 1, 0]

        def dfs(i, j, s):
            if not s:
                return True
            if board[i][j] != s[0]:
                return False
            if board[i][j] == s:
                return True
            V[i][j] = True
            for di in range(0, len(direction) - 1):
                r = i + direction[di]
                c = j + direction[di + 1]
                if 0 <= r < m and 0 <= c < n:
                    if V[r][c] == False:
                        res = dfs(r, c, s[1:])
                        if res == True:
                            return True
            V[i][j] = False
            return False

        for ri in range(0, m):
            for ci in range(0, n):
                if dfs(ri, ci, word):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    l = [["a","a"]], "aaa"
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    r = s.exist(*l)
    # 174801674
    print(r)
