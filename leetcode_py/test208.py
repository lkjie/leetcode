
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter, defaultdict
from typing import List

from collections import defaultdict

class LinkNode:
    def __init__(self, isleaf=False):
        self.isleaf = isleaf
        self.next = defaultdict(LinkNode)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = LinkNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pnode = self.root
        for i, s in enumerate(word):
            if s not in pnode.next:
                pnode.next[s] = LinkNode(False)
            pnode = pnode.next[s]
        pnode.isleaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pnode = self.root
        for s in word:
            if s not in pnode.next:
                return False
            pnode = pnode.next[s]
        return len(pnode.next) == 0 and pnode.isleaf

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pnode = self.root
        for s in prefix:
            if s not in pnode.next:
                return False
            pnode = pnode.next[s]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    s = Trie()
    r = s.insert('apple')
    r = s.search('apple')
    r = s.search('app')
    r = s.insert('app')
    r = s.search('app')
    print(r)
