class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula for area: min height(b1,b2) * width, width = b2 - b1
        l = 0
        r = len(heights) -1
        area = 0
        max_height = max(heights[l],heights[r])
        while (l < r):
            area = max(area,min(heights[l], heights[r]) * (r - l))

            if(heights[l] < heights[r]):
                l = l +1
            elif(heights[l] > heights[r]):
                r = r - 1
            else:
                l = l + 1 
            # if(heights[l] < max_height):
            #     max_height = max(max_height, heights[l])
            #     l = l + 1
                
            # # if current is less than next
            # if(heights[r] < max_height):
            #     max_height = max(max_height, heights[r])
            #     r = r - 1
            # else:
            #     break
                

        return area
        