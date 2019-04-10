#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>    // std::min_element, std::max_element
#include <initializer_list>
#include <unordered_set>
#include <unordered_map>
#include <limits.h>

namespace hu {
    int minus(int x, int y) { return x - y; }

    int add(int x, int y) { return x + y; }

    int multiply(int x, int y) { return x * y; }
}
using namespace std;

class Solution {
private:
    unordered_map<string, vector<int>> m;

    vector<int> ways(string input) {
        if (m.count(input)) return m[input];
        vector<int> ans;
        for (int i = 0; i < input.length(); ++i) {
            auto op = input[i];
            if (op == '+' || op == '-' || op == '*') {
                string l = input.substr(0, i);
                string r = input.substr(i + 1);
                auto left = ways(l);
                auto right = ways(r);
                std::function<int(int, int)> f;
                switch (op) {
                    case '+':
                        f = hu::add;
                        break;
                    case '-':
                        f = hu::minus;
                        break;
                    case '*':
                        f = hu::multiply;
                        break;
                }
                for (auto &li : left) {
                    for (auto &ri: right) {
                        ans.push_back(f(li, ri));
                    }
                }
            }
        }
        if (ans.empty()) ans.push_back(std::stoi(input));
        return m[input] = ans;
    }

public:
    vector<int> diffWaysToCompute(string input) {
        return ways(input);
    }

    void print(vector<int> vec) {
        for (auto i : vec) {
            cout << i << " ";
        }
        cout << endl;
    }
};

int main() {
    string nums = "2*3-4*5";
    Solution sol = Solution();
    sol.print(sol.diffWaysToCompute(nums));
    return 0;
}
