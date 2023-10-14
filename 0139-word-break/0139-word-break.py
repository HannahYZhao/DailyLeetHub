"""
We'll define a boolean array dp of length n+1, where n is the length of the input string s. dp[i] will be true if the substring s[0:i] can be segmented into space-separated sequences of words from the wordDict.

The idea is to iterate through the string s and check if any substring ending at index i can be formed using words from the wordDict. To do this, we'll check if there is any index j such that dp[j] is true (meaning s[0:j] can be segmented) and the substring s[j:i] (s[j:i] is the substring from index j to i-1) is present in the wordDict.
"""
# Time complexity O(n^2)
# Space complexity O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n= len(s)
        dp= [False] * (n+1)
        dp[0]= True

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[n]