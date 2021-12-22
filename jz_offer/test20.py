# -*- coding:utf-8 -*-
class Solution:
    s = []
    s_sort = []
    def push(self, node):
        # write code here
        self.s.append(node)
        si = 0
        ei = len(self.s_sort) - 1
        if len(self.s_sort) == 0:
            self.s_sort.insert(0, node)
            return
        if self.s_sort[0] >= node:
            self.s_sort.insert(0, node)
            return
        if self.s_sort[-1] <= node:
            self.s_sort.insert(ei+1, node)
            return
        while si <= ei:
            s_mid = int((si + ei) / 2)
            if self.s_sort[s_mid] == node:
                si = ei = s_mid
                break
            elif self.s_sort[s_mid] < node:
                si = s_mid + 1
            else:
                ei = s_mid - 1
        self.s_sort.insert(ei+1, node)
    def pop(self):
        # write code here
        return self.s.pop(-1)
    def top(self):
        # write code here
        return self.s[-1]
    def min(self):
        # write code here
        return self.s_sort[0]



if __name__ == '__main__':
    s = Solution()
    s.push(3)
    s.push(4)
    s.push(2)
    s.push(5)
    s.push(1)