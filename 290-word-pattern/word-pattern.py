class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_index_s = {}
        char_index_t = {}

        for i in range(len(pattern)):
            if pattern[i] not in char_index_s:
                char_index_s[pattern[i]] = i

            if words[i] not in char_index_t:
                char_index_t[words[i]] = i

            if char_index_s[pattern[i]] != char_index_t[words[i]]:
                return False

        return True