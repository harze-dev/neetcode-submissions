class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for x in range(len(s)):
            if s[x] in ds:
                ds[s[x]] = ds[s[x]] + 1
            else:
                ds[s[x]] = 1

        for x in range(len(t)):
            if t[x] in dt:
                dt[t[x]] = dt[t[x]] + 1
            else:
                dt[t[x]] = 1
        
        return ds == dt

        