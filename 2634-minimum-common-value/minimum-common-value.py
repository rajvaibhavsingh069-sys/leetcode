class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        for x in nums1:
            l, r = 0, len(nums2) - 1

            while l <= r:
                m = (l + r) // 2

                if nums2[m] == x:
                    return x
                elif nums2[m] < x:
                    l = m + 1
                else:
                    r = m - 1

        return -1