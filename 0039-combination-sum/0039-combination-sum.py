# Backtracking-based solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def helper(i, path):
            # We have found our answer, lets return...
            # endpoint 1(we found a matching target)
            if sum(path) == target:
                results.append(path[:])
                return

            # endpoint 2(the sum is greater than the target)
            if sum(path) > target:
                return

            # With each iteration of the for loop, we will reduce the number of candidates, this is important to prevent duplicates
            for x in range(i, len(candidates)):
                # Lets keep adding to path.
                path.append(candidates[x])
                # Lets run combination again, if the path is not our target length, it will go to the for loop again.
                helper(x, path)
                # Backtrack, remove my last element, so I can move on.
                path.pop()

        helper(0, [])
        return results