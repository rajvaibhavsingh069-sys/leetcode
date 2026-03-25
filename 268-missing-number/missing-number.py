class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        i=0

        while i<n:
            cur=nums[i]
            if nums[i]<n and nums[i]!=nums[cur]:
                nums[i],nums[cur]=nums[cur],nums[i]
            else: i+=1
            


        for i in range (n):
            if (nums[i]!=i):
                return i
        return n


        