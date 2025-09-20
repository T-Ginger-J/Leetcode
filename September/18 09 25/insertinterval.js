/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    const result = [];
    let i = 0;

    // Add all intervals ending before newInterval starts
    while (i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }

    // Merge all overlapping intervals into newInterval
    while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    result.push(newInterval);

    // Add remaining intervals
    while (i < intervals.length) {
        result.push(intervals[i]);
        i++;
    }

    return result;
};

const insertOneLine = (A,I) => (A.reduce((r,x)=>(I&&I[1]<x[0]?(r.push(I),I=null):I&&I[0]<=x[1]?(I=[Math.min(I[0],x[0]),Math.max(I[1],x[1])]):r.push(x),r),[])).concat(I? [I]:[]);

console.log(insert([[1,3],[6,9]],[2,5])); 
// [[1,5],[6,9]]

console.log(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]));
// [[1,2],[3,10],[12,16]]
