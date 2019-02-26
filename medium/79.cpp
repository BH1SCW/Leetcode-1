#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>    // std::min_element, std::max_element
#include <initializer_list>
#include <utility>
#include <unordered_set>


using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>> &board, string word) {
        int m = board.size(), n = board[0].size();
        std::function<bool(int, int, int)> dfs = [&](int i, int j, int index) {
            // cout << i << " " << j << " " << index << endl;
            if (index >= word.length()) return true;
            if (i < 0 || i >= m || j < 0 || j >= n || (board[i][j] == '\0') || string({1, board[i][j]}) != string({1, word[index]})) {
                // cout << board[i][j] << " " << word[index] << " " << index << endl;
                return false;
            }
            auto t = board[i][j];
            // cout << t << endl;
            board[i][j] = '\0';
            if (dfs(i + 1, j, index + 1) || dfs(i - 1, j, index + 1) || dfs(i, j - 1, index + 1) || dfs(i, j + 1, index + 1)) {
                board[i][j] = t;
                return true;
            }
            board[i][j] = t;
            return false;
        };
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dfs(i, j, 0))
                    return true;
            }
        }
        return false;
    }
};


int main() {
    vector<vector<char>> board = {{'A', 'B', 'C', 'E'},
                                  {'S', 'F', 'C', 'S'},
                                  {'A', 'D', 'E', 'E'}};
    string word = "ABCCED";
    // string word = "SEE";
    // string word = "ABCB";


    Solution sol = Solution();
    cout << sol.exist(board, word) << endl;
    return 0;
}