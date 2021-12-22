#include <iostream>
#include <string>
#include<algorithm>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    // v1
//    int maxArea(vector<int>& height) {
//        set<int> eleset(height.begin(), height.end());
//        vector<int> eles(eleset.begin(), eleset.end());
//        sort(eles.begin(), eles.end(), greater<int>());
//        int max_size = 0;
//        for (int i=0;i < eles.size(); i++){
//            int max_y = eles[i];
//            int left_x = 0;
//            int right_x = height.size()-1;
//            while (left_x<right_x){
//                if (height[left_x]>=max_y && height[right_x]>=max_y){
//                    max_size = max(max_size, max_y * (right_x - left_x));
//                    break;
//                }
//                if (height[left_x]<max_y){left_x++;}
//                if (height[right_x]<max_y){right_x--;}
//            }
//        }
//        return max_size;
//    }

    int maxArea(vector<int>& height) {
        int max_size = 0;
        int left_x = 0;
        int right_x = height.size()-1;
        int left_max_height = height[0];
        int right_max_height = height[right_x];
        while (left_x<right_x){
            max_size = max(max_size, min(left_max_height, right_max_height) * (right_x - left_x));
            if (height[left_x] < height[right_x]){
                // move left
                int old_left_x = left_x;
                for (++left_x; left_x < height.size(); ++left_x) {
                    if(height[left_x]>height[old_left_x]){
                        left_max_height = height[left_x];
                        break;
                    }
                }
            } else{
                // move right
                int old_right_x = right_x;
                for (--right_x; right_x > 0; --right_x) {
                    if(height[right_x]>height[old_right_x]){
                        right_max_height = height[right_x];
                        break;
                    }
                }
            }
        }
        return max_size;
    }
};


int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution s;
    vector<int> v = {1,8,6,2,5,4,8,3,7};
    std::cout << s.maxArea(v);
    return 0;
}