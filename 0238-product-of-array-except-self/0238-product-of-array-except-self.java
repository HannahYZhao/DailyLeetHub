/**
 * Four steps of thinking when interviews
 * 1. Brute Force thinking really straight forward, just as a direct translate for the description
 * There would be two variables j and index i, the time complexity for this solution would be O(n*2).
 * Thinking about optimize the time complexity of the solution.
 * 2. Dividing the product of array with the number
 * ans[i] = pro / nums[i] Didn't think of 0 in our array
 * We need to think of a way using multiplication.
 * 3. Finding Prefix Product and Suffix Product
 * ans[i] = pre[i] * suff[i] The time complexity would be O(n), but we are now using Auxilary space of O(n)
 * To optimize the space complexity of the program
 * 4. Directly store the product of prefix and suffix into the final answer array
 */


// Time complexity: O(n)
// Space complexity: O(1)
class Solution {
    public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int ans[] = new int[n];
    Arrays.fill(ans, 1);
    int curr = 1;
    for(int i = 0; i < n; i++) {
        ans[i] *= curr;
        curr *= nums[i];
    }
    curr = 1;
    for(int i = n -1; i >= 0; i--) {
        ans[i] *= curr;
        curr *= nums[i];
    }
    return ans;
}
}