#include <functional>
#include <queue>
#include <vector>
#include <list>
#include <iostream>
#include <unordered_map>
#include <unordered_set>


using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_set<string> set;
        unordered_map<string, int> counter;
        unordered_map<string, int> target;
        int ans = -1;
        list<int> temp;
        for (int i = 0; i < t.size(); i++) {
            target.find(t[i]) == target.end() ? target[t[i]] = 1 : target[t[i]]++;
        }
        for (int i = 0; i < s.size(); i++) {
            target.find(s[i]) == target.end() ? : temp.push_back(i);
        }
        vector<int> index.reserve(temp.size());
        std::copy(temp.begin(), temp.end(), back_inserter(index));
        counter[t[index[0]]] = 1;
        int i = index[0], j = i;
        while (true) {
        }
    }
};

int main() {
    String s = "ADOBECODEBANC";
    String t = "ABC";
    Solution sol = Solution();
    cout << sol.minWindow(s, t) << endl;
    return 0;
}
