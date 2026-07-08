class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for x in range(len(nums)):
            if nums[x] in h: # found pair
                return [h[nums[x]], x] # first indice, matching indice
            else: # add key (number we are looking for) and value (indice of original)
                h[target - nums[x]] = x
        