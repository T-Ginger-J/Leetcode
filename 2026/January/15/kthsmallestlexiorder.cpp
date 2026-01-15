// LeetCode 440: K-th Smallest in Lexicographical Order
// Time Complexity: O(log^2 n)
// Space Complexity: O(1)

class Solution {
public:
    int findKthNumber(int n, int k) {
        long curr = 1;
        k--;

        while (k > 0) {
            long steps = countSteps(n, curr, curr + 1);
            if (steps <= k) {
                curr++;
                k -= steps;
            } else {
                curr *= 10;
                k--;
            }
        }
        return (int)curr;
    }

private:
    long countSteps(int n, long first, long last) {
        long steps = 0;
        while (first <= n) {
            steps += min((long)n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    }
};

int main() {
    Solution sol;

    // Example 1: Small n, small k
    cout << sol.findKthNumber(13, 2) << endl;
    // Expected output: 10

    // Example 2: k points to the last element
    cout << sol.findKthNumber(20, 20) << endl;
    // Expected output: 9

    // Example 3: n crosses a power-of-10 boundary
    cout << sol.findKthNumber(100, 90) << endl;
    // Expected output: 9

    return 0;
}