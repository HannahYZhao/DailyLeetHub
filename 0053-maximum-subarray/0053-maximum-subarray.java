class Solution {
    public int maxSubArray(int[] nums) {
        // Initialize currMaxSum & take first element of array from which we start tp do sum...
        int maxSum = nums[0];
        // Initialize the current sum of our subarraay as nums[0]...
        int currSum = nums[0];
        // Traverse all the element through the loop...
        for(int i = 1; i < nums.length; i++) {
            // Do sum of elements contigous with curr sum...
            // Compare it with array element to get maximum result...
            currSum = Math.max(currSum + nums[i], nums[i]);
            // Compare current sum add max sum.
            maxSum = Math.max(maxSum, currSum);
        }
        return maxSum;
    }
}