class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        for c in magazine:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for i in ransomNote:
            if i not in freq:
                return False
            elif freq[i] == 1:
                del freq[i]
            else:
                freq[i] -= 1

        return True