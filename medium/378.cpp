#include <functional>
#include <queue>
#include <vector>
#include <iostream>

using namespace std;


class Solution {
    template<typename T>
    void print_queue(T &q) {
        while (!q.empty()) {
            std::cout << q.top().value << " ";
            q.pop();
        }
        std::cout << '\n';
    }

private:
    class Element {
    public:
        int value, row, col;

        Element(int v, int i, int j) : value(v), row(i), col(j) {
            // value = v;
            // row = i;
            // col = j;
        }
    };

public:
    int kthSmallest(vector<vector<int>> &matrix, int k) {
        auto cmp = [](Element &a, Element &b) { return a.value > b.value; };
        std::priority_queue<Element, std::vector<Element>, decltype(cmp)> q(cmp);
        int cols = matrix[0].size();
        for (int i = 0; i < cols; ++i)
            q.push(Element(matrix[0][i], 0, i));
        //print_queue(q);
        for (int i = 0; i < k - 1; ++i) {
            auto _ = q.top();
            q.pop();
            if (_.row + 1 < matrix.size())
                q.push(Element(matrix[_.row + 1][_.col], _.row + 1, _.col));
        }
        return q.top().value;
    }
};

int main() {
    vector<vector<int>> matrix = {{1,  5,  9},
                                  {10, 11, 13},
                                  {12, 13, 15}};
    int k = 8;
    Solution sol = Solution();
    cout << sol.kthSmallest(matrix, k) << endl;
    return 0;
}

