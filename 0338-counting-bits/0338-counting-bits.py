class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            # Now we will add the no of 1's to ans
            result[i] = 1 + result[i - offset]
        
        return result