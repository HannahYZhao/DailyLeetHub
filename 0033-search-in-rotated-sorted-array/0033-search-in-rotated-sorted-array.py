# Binary search approach is based on the fact that a rotated sorted array can be divided into two sorted arrays.
# Time complexity: Brute force approach is O(n), Binary search approach is O(log n)
# Space complexity: O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        mid = (start + end) / 2
        while start <= end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target and nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return - 1

