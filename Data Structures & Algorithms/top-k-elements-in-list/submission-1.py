class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # count freq.
        for num in nums:
            d[num] = d.get(num,0) + 1

        # sort dict by freq. (desc.)
        ans = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        # list of top k keys
        l = list(ans.keys())
        return l[:k]
        