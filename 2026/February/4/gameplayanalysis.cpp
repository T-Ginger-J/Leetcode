// LeetCode 511: Game Play Analysis I
// Method: Hash Map + Min Date
// Time Complexity: O(n)
// Space Complexity: O(n)

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    vector<tuple<int,int,string,int>> activity = {
        {1,2,"2016-03-01",5},
        {1,2,"2016-05-02",6},
        {2,3,"2017-06-25",1},
        {3,1,"2018-07-10",0},
        {3,1,"2018-07-09",1}
    };

    unordered_map<int,string> first;
    for (auto &[pid, did, date, gp] : activity) {
        if (!first.count(pid) || date < first[pid])
            first[pid] = date;
    }

    for (auto &[pid, date] : first) {
        cout << pid << " " << date << endl;
    }

    // Expected output (order may vary):
    // 1 2016-03-01
    // 2 2017-06-25
    // 3 2018-07-09

    return 0;
}
