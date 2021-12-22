#include <iostream>
#include <string>
#include <vector>

using namespace std;


class Solution {
public:
    string isMatch(string s, string p) {

        if (numRows == 1) return s;

        vector<string> rows(min(numRows, int(s.size())));
        int curRow = 0;
        bool goingDown = false;

        for (char c : s) {
            rows[curRow] += c;
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }

        string ret;
        for (string row : rows) ret += row;
        return ret;
    }
};


int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution s;
    s.convert("LEETCODEISHIRING", 4);
    return 0;
}