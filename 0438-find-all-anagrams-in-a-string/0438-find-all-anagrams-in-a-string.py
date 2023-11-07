# Time complextity: O(n)
# Space complexity: O(n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        mapper = {}
        def __mapper():
            nonlocal mapper
            for i in p:
                if i in mapper.keys(): mapper[i] += 1
                else: mapper[i] = 1

        __mapper()
        ans = []
        st = 0
        ed = 0
        while ed < len(s):
            if s[ed] in mapper.keys():
                #-= 1 is the shorthand notation for subtracting 1 from the current value. In other words, it decrements the count of the character s[ed] in the mapper dictionary. It's a concise way of expressing mapper[s[ed]] = mapper[s[ed]] - 1.
                mapper[s[ed]] -= 1         
                if mapper[s[ed]] == 0:
                    del mapper[s[ed]]
                if not bool(mapper):
                    ans.append(st)
                    mapper[s[st]] = 1
                    st += 1
                ed += 1
            else:
                if st == ed:
                    st = ed = ed + 1
                else:
                    if s[st] in mapper.keys():
                        mapper[s[st]] += 1
                    else:
                        mapper[s[st]] = 1
                    st += 1
        return ans
