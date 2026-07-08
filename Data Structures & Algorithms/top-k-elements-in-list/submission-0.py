class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1

        ans = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        l = list(ans.keys())
        return l[:k]
        