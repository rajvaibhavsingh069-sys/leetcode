class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        l=0
        count=0
        n =len(s)
        for r in range(n):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1

            Set.add(s[r])
            count=max(count,r-l+1)
        return count