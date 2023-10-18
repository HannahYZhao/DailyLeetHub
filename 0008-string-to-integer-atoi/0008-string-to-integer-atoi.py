# Time complexity: O(log(x))
# Space complexity: O(1)
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading and trainling whitespace
        """
        example of strip syntx in python:
        txt = ",,,,,rrttgg.....banana....rrr"
        x = txt.strip(",.grt")
        print(x)
        result:banana
        """
        s = s.strip( )
        if not s:
            # Handle empty string case
            return 0
        num = 0
        i = 0
        # 1 for postive, -1 for negative
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        # Check for integer overflow
        num = max(min(num, 2 ** 31 - 1), -2 ** 31)
        return num