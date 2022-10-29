class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        unique_lists = list(set([points[i][0] for i in range(len(points))]))
        unique_lists.sort()
        
        max_width = 0
        for i in range(len(unique_lists)-1):
            width = unique_lists[i+1] - unique_lists[i]
            if width > max_width:
                max_width = width
            
        return max_width