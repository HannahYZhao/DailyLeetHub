class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create an array...
        arr = []
        arr.append(nums[0])
        # Initialize the max sum...
        maxSum = arr[0]
        # Traverse all the element through the loop...
        for i in range(1, len(nums)):
            # arr[i - 1] + nums[i](largest sum plus current number with suing prefix)
            # calculare arr[0], arr[1]..., arr[n] while comparing each one with current largest sum...
            arr.append(max(arr[i - 1] + nums[i], nums[i]))
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum
        