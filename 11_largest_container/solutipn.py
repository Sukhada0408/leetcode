class Solution:
    def maxArea(self, height: list[int]) -> int:
        length = len(height)
        area = 0
        p1 = 0
        p2 = length-1
        while p1<=p2:
            A = min(height[p1], height[p2])*(p2-p1)
            area = max(area, A)
            if height[p1]<=height[p2]:
                p1+=1
            else:
                p2-=1
        return area