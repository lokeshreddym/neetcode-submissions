class Solution:
    def trap(self, height: List[int]) -> int:


        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        # left to right pass
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])

        # right to left pass
        right_max[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        water = 0
        for i in zip(left_max,right_max,height):
            water += min(i[0],i[1])-i[2]
        return water


        
        