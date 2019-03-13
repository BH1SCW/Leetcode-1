#include <iostream>
#include <string>
#include <map> 
#include <list> 
#include <vector> 
#include <bits/stdc++.h> 
using namespace std;

std::map<float, string> translation = {
                                 {0.01,  "PENNY"},
                                 {0.05,  "NICKEL"},
                                 {0.1,  "DIME"},
                                 {0.25,  "QUARTER"},
                                 {0.5,  "HALF DOLLAR"},
                                 {1.0,  "ONE"},
                                 {2.0,  "TWO"},
                                 {5.0,  "FIVE"},
                                 {10.0,  "TEN"},
                                 {20.0,  "TWENTY"},
                                 {50.0,  "FIFTY"},
                                 {100.0,  "ONE HUNDRED"}

};

std::vector<float> money {0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0};

std::list<float> answer;

// get the largest possible bill
float findClosest(float cash) {
  for (int i = money.size() - 1; i >= 0; i--) {
    if (money[i] <= cash) {
      return money[i];
    }
  }
}

void getChange(float cash) {
  float bill = findClosest(cash);
  // cout << "closet to " << cash << " is " << bill << endl;
    answer.push_back(bill);
  // catch exception
  // there is precision problem
  if (cash - bill < 0.01) {
    /*if (cash - bill > 0) {
      try {
          throw cash;
        }
      catch (float cash) {
          cout << "An exception occurred. " << cash << "is smaller than a penny." << '\n';
        }
    } else {*/
      for (auto a = answer.begin(); a!= answer.end(); ) {
        cout << translation[*a];
        if (++a != answer.end()) cout << ",";
        else cout << endl;
      }
      answer.clear();
    //};
  } else {
    getChange(cash - bill);
  }
}

// parse string
std::pair<float, float> parse(stringstream line) {
  std::pair<float, float> ans;
  string temp;
  getline(line, temp,';');
  ans.first = stof(temp);
  getline(line, temp, ';');
  ans.second = stof(temp);
  return ans;
}

int main() {
  string line;
  std::pair<float, float> input;
  while (getline(cin, line)) {
    input = parse(stringstream(line));
    if (input.first > input.second) cout << "ERROR" << endl;
    if (input.first == input.second) cout << "ZERO" << endl;
    if (input.first < input.second) getChange(input.second - input.first);
  }
  return 0;
}
