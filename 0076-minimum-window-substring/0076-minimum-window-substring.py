class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        map = {}
        for char in t:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        count = 0
        start = 0
        min_length = float("inf")
        min_start = 0
        for end in range(len(s)):
            if s[end] in map:
                map[s[end]] -= 1
                if map[s[end]] >= 0:
                    count += 1
            while count == len(t):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    min_start = start
                if s[start] in map:
                    map[s[start]] += 1
                    if map[s[start]] > 0:
                        count -= 1
                start += 1
        return "" if min_length == float("inf") else s[min_start:min_start+min_length]
                