// LeetCode 452: Minimum Number of Arrows to Burst Balloons
// Alternate perspective: Greedy by maintaining intersection window
// - Sort by start coordinate
// - Maintain the current overlapping window [left, right]
// - When a balloon does not overlap, fire an arrow and reset window
//
// Time Complexity: O(n log n)
// Space Complexity: O(1)

var findMinArrowShots = function(points) {
    if (points.length === 0) return 0;

    points.sort((a, b) => a[0] - b[0]);

    let arrows = 1;
    let left = points[0][0];
    let right = points[0][1];

    for (let i = 1; i < points.length; i++) {
        const [s, e] = points[i];
        if (s > right) {
            arrows++;
            left = s;
            right = e;
        } else {
            left = Math.max(left, s);
            right = Math.min(right, e);
        }
    }
    return arrows;
};

// Additional Examples

// Example 1: Overlapping intervals
console.log(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]));
// Expected output: 2

// Example 2: No overlaps
console.log(findMinArrowShots([[1,2],[3,4],[5,6]]));
// Expected output: 3

// Example 3: All balloons overlap
console.log(findMinArrowShots([[1,10],[2,9],[3,8],[4,7]]));
// Expected output: 1
