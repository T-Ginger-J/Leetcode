/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    const res = [];
    if (nums.length === 0) return res;

    let start = nums[0];

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1] + 1) {
            if (start === nums[i - 1]) res.push(String(start));
            else res.push(start + "->" + nums[i - 1]);
            start = nums[i];
        }
    }

    if (start === nums[nums.length - 1]) 
        res.push(String(start));
    else 
        res.push(start + "->" + nums[nums.length - 1]);

    return res;
};
