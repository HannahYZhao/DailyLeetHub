# It reads the same from forward and backword - palindromic
        # odd case, like "aba"
        # self.helper is a method call to the helper method, which is designed to find palindromic substrings
        # aba = isi?
        # even case, like "abba"
        # The reason for using i+1 is because it is necessary to consider both the character at index i and the character immediately to the right of it (at index i+1) as the potential center for even-length palindromes.
        # (in this case, "bb" at indices i and i+1)
class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
