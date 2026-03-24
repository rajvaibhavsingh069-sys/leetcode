class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        n=len(height)
        l=0
        r=n-1
        
        while l<r:
            area= (r-l)*min(height[r],height[l])
            res=max(res,area)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            
        return res
    