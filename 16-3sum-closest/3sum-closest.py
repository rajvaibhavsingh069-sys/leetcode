class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)

        closest = float('inf')

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if (sum - target) * (sum - target) < (closest - target) * (closest - target):
                    closest=sum
                elif sum==target:
                    return sum
                elif sum<target:
                    l+=1
                else:
                    r-=1
        return closest
        

        