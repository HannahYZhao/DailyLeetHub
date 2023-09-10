/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
 // Sort approach
 /**
 Need to compute all distance, we just omit the sqrt and just do x^2 + y^2
 Need to sort by the distance: best: n log(n)
 Do quicksort with a custom sorting function, then take the first k elements from the array
  */
 // Time complexity: O(nlog(n))
 // Space complexity: O(1)
var kClosest = function(points, k) {
    // (a, b) => a - b is a shortcut notation for:
    // function (a, b){
    //   return a - b;
    // }
    points.sort((a, b) => (a[0]*a[0] + a[1]* a[1]) - (b[0]*b[0] + b[1]*b[1]))
    // Array.slice() returns selected array elements as a new array
    return points.slice(0, k)
};