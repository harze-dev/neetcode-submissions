class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for x in range(len(nums)):
            if nums[x] in h:
                return [h[nums[x]], x]
            else:
                h[target - nums[x]] = x
        