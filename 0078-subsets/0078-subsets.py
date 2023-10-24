# Time Complexity: O(2^n) - There are 2^n possible subsets for n elements.
# Space Complexity; O(n) - At most, the depth of the recursion is n, and 'twos' holds a maximum of n elements at any given time.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        twos = []

        def helper_method(start):
            result.append(twos[:])

            for i in range(start, len(nums)):
                if nums[i] not in twos:
                    twos.append(nums[i])
                    helper_method(i + 1)
                    twos.pop()

        helper_method(0)
        return result



        