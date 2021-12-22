
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''
from collections import Counter

c1 = Counter()
c2 = Counter()
print(c1)
print(c2)
print(c1 == c2)


class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        word_size = len(words[0])
        if len(s) < len(words) * word_size:
            return []
        from collections import Counter
        res = []
        c1 = Counter(words)
        for i in range(0, word_size):
            idx = i
            c2 = Counter()
            while idx + word_size <= len(s):
                if sum(c2.values()) < len(words):
                    c2.update([s[idx:idx+word_size]])
                    idx += word_size
                else:
                    if c1 == c2:
                        res.append(idx-word_size*len(words))
                    c2 -= Counter([s[idx-word_size*len(words):idx-word_size*(len(words)-1)]])
            if c1 == c2:
                res.append(idx-word_size*len(words))
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))