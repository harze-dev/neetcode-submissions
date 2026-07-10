class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for s in s1:
            d[s] = d.get(s, 0) + 1

        l = 0
        s1_length = len(s1)
        d2 = {}
        for x in range(len(s2)):

            d2[s2[x]] = d2.get(s2[x], 0) + 1 
            if(x-l + 1 == s1_length and d2 == d):
                return True
            elif(x-l + 1 == s1_length):
                d2[s2[l]] = d2.get(s2[l], 0) - 1
                d2 = {key: val for key, val in d2.items() if val != 0}
                l = l + 1

        return False
            
        