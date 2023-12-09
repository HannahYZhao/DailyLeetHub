class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # sorted(..., key=lambda v: v[1]): This part takes the list of tuples created in step 1 and sorts them based on the second element of each tuple, which is the end time (endTime). The key parameter specifies a function (lambda v: v[1]) that extracts the end time from each tuple for the sorting comparison. This means that the list of jobs will be sorted in ascending order of their end times.


        jobs = sorted(zip(startTime, endTime, profit), key = lambda v: v[1])
        # Intial dp[0] = 0, as we make profit = 0 at time = 0.
        dp = [[0, 0]]
        # s, e, p are its start time, end time and profit
        for s, e, p ,in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]