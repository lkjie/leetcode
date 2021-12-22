# -*- coding:utf-8 -*-
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.first = None
        self.pre = None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        def dfs(node):
            if not node:
                return node
            dfs(node.left)
            if self.first is None:
                self.first = node
                self.pre = node
            else:
                if self.pre:
                    self.pre.right = node
                self.pre = node
            dfs(node.right)
        dfs(root)
        # 单转双
        p = self.first
        while p.right:
            p_next = p.right
            p_next.left = p
            p = p_next
        p.right = self.first
        self.first.left = p
        return self.first


if __name__ == '__main__':

    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(4)
    p5 = Node(5)
    p4.left = p2
    p4.right = p5
    p2.left = p1
    p2.right = p3

    s = Solution()
    r = s.treeToDoublyList(p4)
    print(r)