#include <stdio.h>
#include <vector>
#include <iostream>     // std::cout
#include <algorithm>

using namespace std;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        vector<int> sorted = vector<int>(nums);
        std::sort(sorted.begin(), sorted.end());
        // for (int i = nums.size() - 1, j = nums.size() / 2 - 1, k = nums.size() / 2; i >= 0; i--) {
        // nums[i] = i % 2 == 0 ? sorted[j--] : sorted[k++] ;
        // }
        for (int i = nums.size() - 1, j = 0, k = i / 2 + 1; i >= 0; i--) {
            nums[i] = i % 2 ? sorted[k++] : sorted[j++] ;
        }
//        for(auto n:nums) cout << n << " ";
//        cout << endl;
    }
};


//class Solution {
//public:
//    void wiggleSort(vector<int>& nums) {
//        vector<int> sorted = vector<int>(nums);
//        std::sort(sorted.begin(), sorted.end());
//        // for (int i = nums.size() - 1, j = nums.size() / 2 - 1, k = nums.size() / 2; i >= 0; i--) {
//        // nums[i] = i % 2 == 0 ? sorted[j--] : sorted[k++] ;
//        // }
//        for (int i = nums.size() - 1, j = 0, k = i / 2 + 1; i >= 0; i--) {
//            nums[i] = i % 2 == 0 ? sorted[k++] : sorted[j++] ;
//        }
////        for(auto n:nums) cout << n << " ";
////        cout << endl;
//    }
//};


int main()
{
    vector<int> nums =  [1, 5, 1, 1, 6, 4];
    Solution sol = Solution();
    sol.wiggleSort(nums);
    return 0;
}

