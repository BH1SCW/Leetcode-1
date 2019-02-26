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
// Only for pairs of std::hash-able types for simplicity.
// You can of course template this struct to allow other hash functions
//    struct pair_hash {
//        template<class T1, class T2>
//        std::size_t operator()(const std::pair<T1, T2> &p) const {
//            auto h1 = std::hash<T1>{}(p.first);
//            auto h2 = std::hash<T2>{}(p.second);
//            // Mainly for demonstration purposes, i.e. works but is overly simple
//            // In the real world, use sth. like boost.hash_combine
//            return h1 ^ h2;
//        }
//    };

    bool exist(vector<vector<char>> &board, string word) {
        unordered_set <unordered_set<int, int>> visited;
        int m = board.size(), n = board[0].size();
        std::function<bool(int, int, int)> dfs = [&](int i, int j, int index) {
            if (index >= word.length()) return true;
            if (i - 1 >= 0) {
                if (visited.find({i - 1, j}) == visited.end() && board[i - 1][j] == word[index]) {
                    visited.insert({i - 1, j});
                    if (dfs(i - 1, j, index + 1)) {
                        visited.erase({i - 1, j});
                        return true;
                    }
                }
            }
            if (i + 1 < m) {
                if (visited.find({i + 1, j}) == visited.end() && board[i + 1][j] == word[index]) {
                    visited.insert({i + 1, j});
                    if (dfs(i + 1, j, index + 1)) {
                        visited.erase({i + 1, j});
                        return true;
                    }
                }
            }
            if (j - 1 >= 0) {
                if (visited.find({i, j - 1}) == visited.end() && board[i][j - 1] == word[index]) {
                    visited.insert({i, j - 1});
                    if (dfs(i, j - 1, index + 1)) {
                        visited.erase({i, j - 1});
                        return true;
                    }
                }
            }
            if (j + 1 < n) {
                if (visited.find({i, j + 1}) == visited.end() && board[i][j + 1] == word[index]) {
                    visited.insert({i, j + 1});
                    if (dfs(i, j + 1, index + 1)) {
                        visited.erase({i, j + 1});
                        return true;
                    }
                }
            }
            return false;
        };
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == word[0]) {
                    visited.insert({i, j});
                    if (dfs(i, j, 1))
                        return true;
                    visited.erase({i, j});
                }
            }
        }
        return false;
    }
};


int main() {
    vector<vector<char>> board = {{'A', 'B', 'C', 'E'},
                                  {'S', 'F', 'C', 'S'},
                                  {'A', 'D', 'E', 'E'}};
    // string word = "ABCCED";
    // string word = "SEE";
    string word = "ABCB";


    Solution sol = Solution();
    cout << sol.exist(board, word) << endl;
    return 0;
}