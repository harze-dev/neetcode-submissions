class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for x in range(len(nums) - 2):
            if (x > 0 and nums[x] == nums[x-1]):
                continue
            l = x + 1
            r = len(nums) - 1
            while(l < r):
                total = nums[x]+ nums[l] + nums[r]
                if(total == 0):
                    ans.append([nums[x], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                    while(l<r and nums[l] == nums[l-1]):
                        l = l + 1
                elif(total > 0):
                    r = r-1
                elif(total < 0):
                    l = l + 1

        return ans
