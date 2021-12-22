
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter, defaultdict
from typing import List

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        dl, dr = 0, 0
        for si in s:
            if si == '(':
                dl += 1
            elif si == ')':
                if dl == 0:
                    dr += 1
                else:
                    dl -= 1
        res = set()
        def dfs(i,lcount,rcount,ldelet,rdelete,path):
            if i == len(s):
                if lcount == rcount and ldelet == rdelete == 0:
                    res.add(path)
                return
            if lcount < rcount:
                return
            if s[i] == '(':
                if ldelet > 0:
                    dfs(i+1,lcount,rcount,ldelet-1,rdelete,path)
                dfs(i+1,lcount+1,rcount,ldelet,rdelete,path+'(')
            elif s[i] == ')':
                if rdelete > 0:
                    dfs(i+1,lcount,rcount,ldelet,rdelete-1,path)
                dfs(i+1,lcount,rcount+1,ldelet,rdelete,path+')')
            else:
                dfs(i+1,lcount,rcount,ldelet,rdelete,path+s[i])
        dfs(0,0,0,dl,dr,'')
        return list(res)



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    s = Solution()
    r = s.removeInvalidParentheses("()())()")
    print(r)
