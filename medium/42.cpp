#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>    // std::min_element, std::max_element
#include <initializer_list>


using namespace std;

class Solution {
public:
    int trap(vector<int> &height) {
        int ans = 0;
        if (height.size() <= 1)
            return 0;
        std::function<void(vector<int>::iterator, vector<int>::iterator)> helper = [&](vector<int>::iterator begin,
                                                                                       vector<int>::iterator end) {
            if (*begin < *end) {
                for (auto iter = next(begin, 1); iter != end ; ++iter) {
                    if (*iter <= *begin) {
                        ans += *begin - *iter;
                    } else {
//                        cout << *begin << " " << *end << " " << ans << endl;
                        helper(iter, end);
                        break;
                    }
                }
            } else {
                for (auto iter = prev(end, 1); iter != begin ; --iter) {
                    if (*iter <= *end) {
                        ans += *end - *iter;
                    } else {
//                        cout << *begin << " " << *end << " " << ans << endl;
                        helper(begin, iter);
                        break;
                    }
                }
            }
        };
        helper(height.begin(), prev(height.end(), 1));
        return ans;
    }
};


int main() {
//    vector<vector<int>> matrix = {{1,  5,  9}, {10, 11, 13}, {12, 13, 15}};
//    vector<vector<int>> matrix = {{1,  4,  7,  11, 15}, {2,  5,  8,  12, 19}, {3,  6,  9,  16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}}
//    vector<vector<int>> matrix = {{9, 9, 4}, {6, 6, 8}, {2, 1, 1}};
//    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    vector<int> height = {6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3};
    Solution sol = Solution();
    cout << sol.trap(height) << endl;
    return 0;
}