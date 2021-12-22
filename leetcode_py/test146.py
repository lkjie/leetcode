from typing import List
from collections import Counter, defaultdict
import copy
class LinkNode:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        assert capacity > 0
        self.l = LinkNode(None)
        self.l.prev = self.l.next = self.l
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.lmap = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.lmap[key]
            nodep = node.prev
            noden = node.next
            nodep.next = noden
            noden.prev = nodep
            nodefirst = self.l.next
            self.l.next = node
            node.next = nodefirst
            node.prev = self.l
            nodefirst.prev = node
        return self.cache.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            node = self.lmap[key]
            nodep = node.prev
            noden = node.next
            nodep.next = noden
            noden.prev = nodep
            nodefirst = self.l.next
            self.l.next = node
            node.next = nodefirst
            node.prev = self.l
            nodefirst.prev = node
        else:
            if self.size == self.capacity:
                nodedel = self.l.prev
                keydel = nodedel.val
                self.cache.pop(keydel)
                self.l.prev = nodedel.prev
                nodedel.prev.next = self.l
                self.lmap.pop(keydel)
                self.size-=1
                self.put(key, value)
            else:
                self.cache[key] = value
                node = LinkNode(key,self.l,self.l.next)
                self.l.next = node
                node.next.prev = node
                self.lmap[key] = node
                self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    # l = [7,1,5,3,6,4]
    # l = [0,1,0,2,1,0,1,3,2,1,2,1]
    obj = LRUCache(2)
    obj.put(1,1)
    obj.put(2,2)
    param_1 = obj.get(1)
    obj.put(3,3)
    param_1 = obj.get(2)
    print(param_1)
    # obj.put(3,2)
    # obj.put(4,2)
    # obj.put(5,2)
    # param_1 = obj.get(1)
    # 174801674
