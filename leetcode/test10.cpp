#include <iostream>
#include <string>
#include <vector>

using namespace std;


class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();

        auto matches = [&](int i, int j) {
            if (i == 0) {
                return false;
            }
            if (p[j - 1] == '.') {
                return true;
            }
            return s[i - 1] == p[j - 1];
        };
        // f[0][0]表示空字符串，f[i][j]表示s的第i个字符于p的第j个字符是否匹配，i/j从1开始，所以在s/p中需要判断s[i-1]与p[j-1]的值

        vector<vector<int>> f(m + 1, vector<int>(n + 1));
        f[0][0] = true;
        for (int i = 0; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '*') {
                    f[i][j] |= f[i-1][j - 1];
                    if (matches(i, j - 1)) {
                        f[i][j] |= f[i - 1][j];
                    }
                }
                else {
                    if (matches(i, j)) {
                        f[i][j] |= f[i - 1][j - 1];
                    }
                }
            }
        }
        return f[m][n];
    }
};


int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution s;
    std::cout << s.isMatch("abc", "ab*");
    return 0;
}