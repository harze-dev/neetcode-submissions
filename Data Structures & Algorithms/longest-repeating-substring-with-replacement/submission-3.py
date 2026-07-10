class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        m = 0
        d = {}
        for x in range(len(s)):
            d[s[x]] = d.get(s[x], 0) + 1
            most_common_char = max(d, key=d.get)
            count = d[most_common_char]
            window_length = x - l + 1
            if not(window_length - count <= k):
                d[s[l]] = d.get(s[l],0) - 1
                l = l + 1
            else:
                m = max(m, window_length)
            
        return m
        