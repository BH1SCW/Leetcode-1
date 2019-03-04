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
   template<class T>
   void print(vector<T> vec) {
       for (auto e : vec) {
           cout << e << " ";
       }
       cout << endl;
   }
   vector<int> productExceptSelf(vector<int>& nums) {
       vector<int> left(nums.size(), 1);
       vector<int> right(nums.size(), 1);
       vector<int> product(nums.size(), 1);
       for (int i = 1; i < nums.size(); i++) {
           left[i] = left[i - 1] * nums[i - 1];
       }
       for (int i = nums.size() - 2; i >= 0; i--) {
           right[i] = right[i + 1] * nums[i + 1];
       }
       for (int i = 0; i < nums.size(); i++) {
           product[i] = left[i] * right[i];
       }
       print(product);
       return product;
   }
};

int main() {
    // vector<int> nums = {1, 2, 3, 4};
    vector<int> nums = {};
    // vector<int> nums = {3,4,-1,1};
    Solution sol = Solution();
    sol.productExceptSelf(nums);
    return 0;
}
