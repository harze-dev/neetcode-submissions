class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}

        if len(s) != len(t):
            return False

        for x in range(len(s)):
            if s[x] in ds:
                ds[s[x]] = ds[s[x]] + 1
            else:
                ds[s[x]] = 1
            if t[x] in dt:
                dt[t[x]] = dt[t[x]] + 1
            else:
                dt[t[x]] = 1
        
        return ds == dt

        