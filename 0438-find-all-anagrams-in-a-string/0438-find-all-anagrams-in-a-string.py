# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # hm is a dictionary (hashmap) that is used to keep track of the character frequencies in the pattern string p. For each character in p, its frequency is stored in the dictionary. pL and sL represent the lengths of strings p and s, respectively.

        hm, res, pL, sL = defaultdict(int), [], len(p),len(s)
        # The code first checks if the length of p is greater than the length of s. If this is the case, there can be no anagrams in s, so it returns an empty list [].
        if pL > sL: return []

        # Build hashmap
        for ch in p: hm[ch] += 1

        # Initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1

        # Slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm:
                hm[s[i+pL]] -= 1

                # Check whether we encountered an anagram
                if all(v == 0 for v in hm.values()):
                    res.append(i+1)
        return res