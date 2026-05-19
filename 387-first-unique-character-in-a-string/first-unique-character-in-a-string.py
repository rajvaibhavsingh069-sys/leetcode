class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for i in s:
            freq[i] = 1 + freq.get(i, 0)
        
        for j, i in enumerate(s):
            if freq[i] == 1:
                return j
        
        return -1