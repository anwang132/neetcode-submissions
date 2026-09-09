class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        ie = len(heights) - 1
        result = 0
        while i < ie:
            if ((ie - i) * min(heights[i], heights[ie]) > result):
                result = (ie - i) * min(heights[i], heights[ie])
            if (heights[ie] < heights[i]):
                ie -= 1
            else:
                i += 1
        return result
