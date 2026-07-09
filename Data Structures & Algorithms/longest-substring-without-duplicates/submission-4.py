class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = 0
        d = set()
        for x in range(len(s)):
            
            
            if s[x] not in d:
                d.add(s[x])
                m = max(m, x - l + 1)
            else:
                while(s[x] in d):
                    d.remove(s[l])
                    # m = max(m, x - l + 1)
                    l = l + 1

                d.add(s[x])
            
            

            
                

        return m