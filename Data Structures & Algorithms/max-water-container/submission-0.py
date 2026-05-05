class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_area=0
        n=len(heights)
        while i<n-1:
            print(i)
            width = j-i
            area = width * min(heights[i],heights[j])
            if area>max_area:
                max_area = area
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            if j==0:
                break
        return max_area

        