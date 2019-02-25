class Solution {
public:
  int uniquePaths(int m, int n) {
    vector<vector<int>> path(m, vector<int> (n, 1));
    for (int i = m - 2; i >= 0; i--) {
      for (int j = n - 2; j >= 0; j--) {
        path[i][j]= path[i][j + 1] + path[i + 1][j];
      }
    }
    return path[0][0];
  }
};

