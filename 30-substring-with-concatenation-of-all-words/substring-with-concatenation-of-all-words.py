class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        from collections import Counter, defaultdict

        if not s or not words:
            return []

        word_len = len(words[0])
        n = len(words)
        total_len = word_len * n
        freq = Counter(words)

        res = []

        for i in range(word_len):
            left = i
            curr = defaultdict(int)
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in freq:
                    curr[word] += 1
                    count += 1

                    while curr[word] > freq[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == n:
                        res.append(left)

                else:
                    curr.clear()
                    count = 0
                    left = right + word_len

        return res