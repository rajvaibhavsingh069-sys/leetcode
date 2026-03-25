class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        for i in range(n):
            xor ^= i ^ nums[i]

        xor ^= n
        return xor 