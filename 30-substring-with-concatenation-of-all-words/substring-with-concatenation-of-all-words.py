class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        res = []

        for i in range(len(s) - total_len + 1):
            seen = []
            
            for j in range(total_words):
                start = i + j * word_len
                word = s[start:start + word_len]
                seen.append(word)

            
            if sorted(seen) == sorted(words):
                res.append(i)

        return res
        