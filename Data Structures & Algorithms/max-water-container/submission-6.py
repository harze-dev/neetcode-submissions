class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula for area: min height(b1,b2) * width, width = b2 - b1
        l = 0
        r = len(heights) -1
        area = 0
        while (l < r):
            area = max(area,min(heights[l], heights[r]) * (r - l))
            
            if(heights[l] < heights[r]): # move left pointer in when shorter than right bar
                l = l +1
            elif(heights[l] > heights[r]): # move right pointer in when shorter than left bar
                r = r - 1
            else: # continue moving pointers as long as l < r
                l = l + 1 
                

        return area
        