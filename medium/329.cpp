#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>    // std::min_element, std::max_element
#include <initializer_list>


using namespace std;

class Solution {
public:
    int longestIncreasingPath(vector<vector<int>> &matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> searched(m, vector<int>(n, 0));
        int ans = 0;
        std::function<int(int, int)> dfs = [&](int i, int j) {
            // cout << "searched " << i << " " << j << " " << searched[i][j] << endl;
            if (searched[i][j])
                return searched[i][j];
            int left = i - 1 >= 0 && matrix[i - 1][j] > matrix[i][j] ? dfs(i - 1, j) : 0;
            int right = i + 1 < m && matrix[i + 1][j] > matrix[i][j] ? dfs(i + 1, j) : 0;
            int up = j - 1 >= 0 && matrix[i][j - 1] > matrix[i][j] ? dfs(i, j - 1) : 0;
            int down = j + 1 < n && matrix[i][j + 1] > matrix[i][j] ? dfs(i, j + 1) : 0;
            int ans = std::max({left + 1, right + 1, up + 1, down + 1});
            searched[i][j] = ans;
//            cout << "dfs: " << i << " " << j << " " << ans << endl;
            return ans;
        };
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!searched[i][j])
                    ans = max(dfs(i, j), ans);
            }
        }
        return ans;
    }
};


int main() {
//    vector<vector<int>> matrix = {{1,  5,  9}, {10, 11, 13}, {12, 13, 15}};
//    vector<vector<int>> matrix = {{1,  4,  7,  11, 15}, {2,  5,  8,  12, 19}, {3,  6,  9,  16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}}
//    vector<vector<int>> matrix = {{9, 9, 4}, {6, 6, 8}, {2, 1, 1}};
    vector<vector<int>> matrix = {{3, 4, 5},
                                  {3, 2, 6},
                                  {2, 2, 1}};
    Solution sol = Solution();
    cout << sol.longestIncreasingPath(matrix) << endl;
    return 0;
}
