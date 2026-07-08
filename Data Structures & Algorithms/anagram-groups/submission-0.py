class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            if tuple(sorted(s)) in d:
                d[tuple(sorted(s))].append(s)
            else:
                key = tuple(sorted(s))
                d.setdefault(key, []).append(s)


        return list(d.values())

        