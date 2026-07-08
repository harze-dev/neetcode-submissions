class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for x in range(len(nums)):
            if nums[x] in table:
                return True
            else:
                table[nums[x]] = x

        return False

        