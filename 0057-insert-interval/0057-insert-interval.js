/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
 // Time complexity: O(n)
var insert = function(intervals, newInterval) {
    const[Start, End] = [0, 1];
    // Start point as well as end point of new interval
    let[s, e] = [newInterval[Start], newInterval[End]];
    // Left: record of intervals on lefthand side
    // Right: record of intervals on righthand side
    let[left, right] = [[], []];
    for(let curInterval of intervals) {
        if(curInterval[End] < s ) {
            // Current interval is on the left hand side of newInterval
            left.push(curInterval);
        }else if(curInterval[Start] > e) {
            // Current interval is on the right hand side of newInterval
            right.push(curInterval);
        }else {
            // Current interval has overlap with newInterval
            // Merge and update boundary
            s = Math.min(s, curInterval[Start]);
            e = Math.max(e, curInterval[End]);
        }
    }
    // The CONCAT function combines the text from multiple ranges and/or strings, but it doesn't provide delimiter or IgnoreEmpty arguments.
    // Syntax CONCAT(text1, [text2],…)
    // text1(required) Text item to be joined. A string, or array of strings, such as a range of cells.
    let result = left.concat([[s,e]]).concat(right);
    return result;
};