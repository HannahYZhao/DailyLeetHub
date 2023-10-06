"""
Classic combinatorial search problem, we can solve it using 3 - step system
1. Identify states
2. Draw the State-space tree
3. DFS on the State-space tree(Using the backtracking template as basis https://algo.monster/problems/backtracking.)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            if len(path) == len(l):
                res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over

The deep copy statement is wrong. This is shallow copy, and it works just fine as we have a list of immutable values (integers). The reason it is needed is that we need a record (copy) of the list when we reach a solution to save the solutions. The list keeps changing, starting from being empty to complete solutions and finally fully empty again. If we only record the reference to it (instead of the copy of the list), we would have a list of identical references that point to a list of empty lists (in fact these empty lists are the same).

                return

            for i, letter in enumerate(l):
                # skip used letters
                if used[i]:
                    continue
                # add letter to permutation, mark letter as used
                path.append(letter)
                used[i] = True
                dfs(path, used, res)
                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False
            
        res = []
        dfs([], [False] * len(l), res)
        return res
"""
class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          
    
    """
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)