
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

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def iterf(node):
            if not node:
                return "null"
            ls = '{}'.format(node.val)
            ls += ',' + iterf(node.left)
            ls += ',' + iterf(node.right)
            return ls

        return iterf(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def iterf(lst):
            if not lst:
                return
            if lst[0] == 'null':
                lst.pop(0)
                return
            n = TreeNode(int(lst[0]))
            lst.pop(0)
            n.left = iterf(lst)
            n.right = iterf(lst)
            return n
        l = data.split(',')
        return iterf(l)

    def deserialize2(self, lst):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        root = TreeNode(lst[0])
        q = [root]
        idx = 1
        while q and idx < len(lst):
            r = q.pop(0)
            if lst[idx] != None:
                n = TreeNode(lst[idx])
                q.append(n)
            else:
                n = None
            idx += 1
            if idx >= len(lst): break
            r.left = n
            if lst[idx] != None:
                n = TreeNode(lst[idx])
                q.append(n)
            else:
                n = None
            r.right = n
            idx += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    s = Codec()
    t = [1,2,3,'null','null',4,5]
    t = map(str,t)
    r = s.deserialize(','.join(t))
    print(r)
