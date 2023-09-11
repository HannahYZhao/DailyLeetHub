/**
 * @param {number[]} nums
 * @return {number[][]}
 */
/**
 * Time complexity:
 * The time complexity of this approach is O(n^2), where n is the size of the input array. 
 * The sorting operation takes O(nlogn) time, and the nested while loop takes O(n^2) time in the worst case.
 * Therefore, the overall time complexity is O(nlogn + n^2) = O(n^2).
 */
 // Time complexity: O(n^2)
 // Space complexity: O(1)
var threeSum = function(nums) {
    const res = [];
    nums.sort((a, b) => a - b);
    // Iterate through the array with a pointer "i" from 0 to n-2, where n is the size of the array
    for(let i = 0; i < nums.length - 2; i++) {
        if(i === 0 || nums[i] !== nums[i - 1]) {
            let lo = i + 1, hi = nums.length - 1, sum = 0 - nums[i];
            while(lo < hi) {
                if(nums[lo] + nums[hi] === sum) {
                    // For each "i", initialize two pointers "lo" and "hi", where "lo" starts at i+1 and "hi" starts at n-1.
                    res.push([nums[i], nums[lo], nums[hi]]);
                    // If the sum is less than zero, increment "lo" to move towards higher values. If the sum is greater than zero, decrement "hi" to move towards lower values
                    while(lo < hi && nums[lo] === nums[lo + 1]) lo++;
                    while(lo < hi && nums[hi] === nums[hi - 1]) hi--;
                    lo++;
                    hi--;
                } else if(nums[lo] + nums[hi] < sum) {
                    lo++;
                } else {
                    hi--;
                }
            }
        }
    }
    return res;
};