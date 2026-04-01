class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray ={0:1}
        cursum = 0
        count=0
        n= len(nums)

        for i in nums:
            cursum +=i

            if cursum -k in subarray:
                count+=subarray[cursum-k]

            subarray[cursum]=1+subarray.get(cursum,0)
        return count