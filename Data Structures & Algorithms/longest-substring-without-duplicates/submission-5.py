class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = 0
        d = set()
        for x in range(len(s)):
            
            # add to set if unique
            if s[x] not in d:
                d.add(s[x])
                # update max substring length
                m = max(m, x - l + 1)
            else:
                # while current is in set, remove duplicates
                while(s[x] in d):
                    d.remove(s[l])
                    l = l + 1

                # add current unique
                d.add(s[x])
            
            

            
                

        return m