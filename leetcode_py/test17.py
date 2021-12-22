import math

class Solution:
    def letterCombinations(self, digits: str):
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        q = [""]
        for si in digits:
            q_new = []
            for s_prefix in q:
                for s_map in phoneMap[si]:
                    q_new.append(s_prefix+s_map)
            q = q_new
        return q



if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))