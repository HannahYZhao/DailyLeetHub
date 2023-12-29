class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # If the list is empty or contains an empty string, return an empty string
        if not strs or "" in strs:
            return ""
        
        ans = ""
        strs = sorted(strs)  # Sort the input list of strings
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans  # Return the common prefix
