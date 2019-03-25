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
 void bfs(int target, vector<int> partial, vector<vector<int>>& result, int index, vector<int>& candidates) {
            if (target == 0) result.push_back(partial);
            if (target > 0) {
                for (int i = index; i < candidates.size();) {
                    int j = i;
                    while (j + 1 < candidates.size() && candidates[j + 1] == candidates[j]) {
                        j++;
                    }
                    vector<int> local(partial.begin(), partial.end());
                    for (int k = i; k < j + 1; k++) {
                        local.push_back(candidates[k]);
                        bfs(target - candidates[i] * (k - i + 1), local, result, j + 1, candidates);
                    }
                    i = j + 1;
                }
            return;
            }
        }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        sort(candidates.begin(), candidates.end());
        bfs(target, {}, result, 0, candidates);
        return result;
    }

    void print(vector<vector<int>> vec) {
        for (auto i : vec) {
            for (auto j : i) {
                cout << j << " ";
        }
        cout << endl;
    }
    }
};

int main() {
    // vector<int> nums = {1, 2, 0};
    vector<int> nums =  {10,1,2,7,6,5};
    int target = 8;
    Solution sol = Solution();
    sol.print(sol.combinationSum2(nums, target));
    return 0;
}