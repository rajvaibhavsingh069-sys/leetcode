class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        nums = [n for n in nums if n>0]
        nums.sort()
        

        Ans = 1
        for n in nums:
            if n==Ans:
                Ans +=1
            elif n>Ans:
                return Ans
        return Ans
        