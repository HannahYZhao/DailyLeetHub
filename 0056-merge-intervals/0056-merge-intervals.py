# Time complexity: O(nlogn). 
"""
In python, use sort method to a list costs O(nlogn).
The for-loop used to merge intervals, costs O(n).
O(nlogn) + O(n) = O(nlogn)
"""
# Space complexity: O(n). n is the length of the input list, the longest solution would be the merged list equals to input intervals list.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            # If the list of merged intervals is empty, or if the current interval does not overlap with the previous, simply append it.
            if merged == []:
                merged.append(intervals[i])
            else:
                previous_end = merged[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                # Otherwise, there is overlap, so we merge the current and previous intervals.
                if previous_end >= current_start: # overlap
                    merged[-1][1] = max(previous_end, current_end)
                else:
                    merged.append(intervals[i])
        return merged