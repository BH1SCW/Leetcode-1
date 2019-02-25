#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target) {
        int m = matrix.size();
        if (m == 0) return false;
        int n = matrix[0].size();
        for (int i = 0, j = n - 1; i < m && j >= 0;) {
            if (matrix[i][j] == target) return true;
            if (matrix[i][j] < target) i++;
            else j--;
        }
        return false;
    }
};


int main() {
//    vector<vector<int>> matrix = {{1,  5,  9}, {10, 11, 13}, {12, 13, 15}};
    vector<vector<int>> matrix = {{1,  4,  7,  11, 15},
                                  {2,  5,  8,  12, 19},
                                  {3,  6,  9,  16, 22},
                                  {10, 13, 14, 17, 24},
                                  {18, 21, 23, 26, 30}}
    int target = 20;
    Solution sol = Solution();
    cout << sol.searchMatrix(matrix, target) << endl;
    return 0;
}

