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

