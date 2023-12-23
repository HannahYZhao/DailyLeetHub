class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Define the base case, and start at 1
        counter = [0]
        # We need to include n, so use n+1 as the bound on the range
        for i in range(1, n+1):
            # Bit-shifting 1 has the same effect as dividing by 2, and is faster, so replace i // 2 with i >> 1
            '''
            Left Shift (<<):0010 << 1 becomes 0100, which is 2 left-shifted by 1 bit to become 4.
            Right Shift (>>): in binary, 0100 >> 1 becomes 0010, which is 4 right-shifted by 1 bit to become 2.
            In many cases, bit-shifting can be faster than division or multiplication because it is a simpler operation at the hardware level. However, in high-level languages like Python, the difference in performance is often negligible because the interpreter or compiler may optimize arithmetic operations like division or multiplication internally.
            '''
            counter.append(counter[i >> 1] + i % 2)
        return counter