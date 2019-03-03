#include <vector>
using namespace std;
int minPower(vector<int> p) {
    auto n = p.size();
    vector<int> solution(n, 1);
    solution[n - 1] = p[n - 1] > 0 ? 1 : -p[n - 1] + 1;
    for (int i = n - 2; i >= 0; --i) {
        if (p[i] < 0)
            solution[i] = -p[i] + solution[i + 1];
        else:
            if (p[i] >= solution[i + 1])
            solution[i] = 1;
            else
                solution[i] = solution[i + 1] - p[i];
    }
    return solution[0];
}
//5 //-5 //4 //-2 //3 //1
1 -2
