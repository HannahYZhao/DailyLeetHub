class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Caculating the max sum of the 2 steps or 3 steps away from the current one, then get the max amount between the two
        max3, max2, ad = 0, 0, 0
        for cur in nums:
            max3, max2, ad = \
            max2, ad, max(max3 + cur, max2 + cur)
        return max(max2, ad)