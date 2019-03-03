#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int rob(vector<int>& points) {
        int prev = points[0], cur = points[1];
        for (int i = 2; i < points.size(); ++i) {
            auto _skip = max(prev, cur);
            auto _take = prev + points[i];
            prev = cur;
            cur = max(_skip, _take);
        }
        return cur;
    }
    int deleteAndEarn(vector<int>& nums) {
        vector<int> points(10001, 0);
        for (auto& n : nums)
            points[n] += n;
        return rob(points);
    }
};
int main() {
    vector<int> nums = {3, 4, 2};
    Solution sol = Solution();
    cout << sol.deleteAndEarn(nums) << endl;
    return 0;
}
