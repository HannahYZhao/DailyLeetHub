class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the input array
        total_sum = sum(nums)

        # If the total sum is odd, we cannot partition the array into two equal sum subsets
        if total_sum % 2 == 1:
            return False
        # Calculate the target sum for each subset
        target_sum = total_sum // 2

        dp = [False] * (target_sum + 1)

        dp[0] = True

        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[target_sum]