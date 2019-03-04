#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>    // std::min_element, std::max_element
#include <initializer_list>
#include <unordered_set>
#include <limits.h>

using namespace std;

class Solution {
public:
    bool isInSet(long e, std::unordered_set<int>& set) {
        return not(set.find(e) == set.end());
    }
    int firstMissingPositive(vector<int>& nums) {
        std::unordered_set<int> set (nums.begin(), nums.end());
        long ans = INT_MAX;
        while (!set.empty()){
            long elem = *set.begin();
            if (elem <= 0) {
                set.erase(elem);
                continue;
            }
            long e  = elem;
            while (isInSet(e - 1, set)){ set.erase(e); e--;
            }
            ans = min(e, ans);
            set.erase(e);
            e= elem + 1;
            while (isInSet(e, set)){ set.erase(e); e++;
            }
        }
        return ans;
    }
};

int main() {
    // vector<int> nums = {1, 2, 0};
    vector<int> nums = {3,4,-1,1};
    Solution sol = Solution();
    cout << sol.firstMissingPositive(nums) << endl;
    return 0;
}
