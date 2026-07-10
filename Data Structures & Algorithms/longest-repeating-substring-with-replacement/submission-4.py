class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        m = 0
        d = {}
        for x in range(len(s)):
            # update freq. of char.
            d[s[x]] = d.get(s[x], 0) + 1
            most_common_char = max(d, key=d.get)
            # most common char. freq.
            count = d[most_common_char]
            
            # size of current window
            window_length = x - l + 1
            
            # if window cannot replace more char.
            if not(window_length - count <= k):
                # decrement freq. of left pointer char.
                d[s[l]] = d.get(s[l],0) - 1
                # move pointer left 1
                l = l + 1
            # otherwise, update max window size
            else:
                m = max(m, window_length)
            
        return m
        