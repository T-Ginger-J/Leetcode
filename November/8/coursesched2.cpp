// LeetCode 210: Course Schedule II
// Explanation:
// 1. Kahn’s algorithm using queue for topological ordering.
// 2. Maintain indegrees, start with 0-indegree courses.
// 3. If all processed → valid order; else → cycle.
// Time Complexity: O(V + E)
// Space Complexity: O(V + E)

#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> graph;
        vector<int> indegree(numCourses, 0);

        for (auto& pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
            indegree[pre[0]]++;
        }

        queue<int> q;
        for (int i = 0; i < numCourses; ++i)
            if (indegree[i] == 0) q.push(i);

    }
};
