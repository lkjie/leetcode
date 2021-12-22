
'''
自己的想法：先列出所有可能，再去除所有的不可能
回溯算法：
dfs：一个字符一个字符的生成
bfs：

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 暴力
        # if not needle:
        #     return 0
        # if len(haystack) < len(needle):
        #     return -1
        # for i in range(0, len(haystack)):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1
        # sunday
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        next_dic = {}
        for i in range(len(needle)-1, -1, -1):
            if needle[i] not in next_dic:
                next_dic[needle[i]] = len(needle) - i
        i = 0
        while i+len(needle) <= len(haystack):
            if haystack[i:i+len(needle)] == needle:
                return i
            else:
                if i+len(needle) >= len(haystack):
                    return -1
                else:
                    i += next_dic.get(haystack[i+len(needle)], len(needle))
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi", 'issi'))