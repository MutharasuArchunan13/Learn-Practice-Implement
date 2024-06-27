from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        previous_hight=0
        stack = []
        for index,h in enumerate(heights):
            if not stack:
               stack.append((index,h))
               previous_hight=h
               continue
            if  h < previous_hight:
                while(stack):
                   i,hh = stack.pop()
                   max_area=max(max_area,hh*(index-i))
            stack.append((i,h))
            previous_hight=h
        return max_area

obj = Solution()
heights=[2,1,5,6,2,3]
result = obj.largestRectangleArea(heights)
print(result)