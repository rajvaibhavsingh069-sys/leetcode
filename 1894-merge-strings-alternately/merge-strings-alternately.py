class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word =[]

        for i,j in zip(word1,word2):
            word.append(i+j)

        word.append(word1[len(word2):])
        word.append(word2[len(word1):])

        return "".join(word)
        