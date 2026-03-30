class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range (n):
            leftsum=0
            rightsum=0
            for j in range (i):
                leftsum+=nums[j]
            for j in range (i+1,n):
                rightsum+=nums[j]
            if leftsum==rightsum:
                return i
        return -1
        