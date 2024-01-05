class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total_gas = 0
        total_cost = 0
        curr_gas = 0
        starting_point = 0

        for i in range(n):
            # These two variables are to check if no case is possible
            total_gas += gas[i]
            total_cost += cost[i]
            # For checking the total present gas at index i
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                # There is a breakdown, so we will start from the next point or index
                starting_point = i + 1
                # Reset our fuel
                curr_gas = 0

        return -1 if total_gas < total_cost else starting_point

        
        