class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        answer = []

        for num in nums:
            digits = []

            while num > 0:
                digits.append(num % 10)
                num //= 10

            digits.reverse()

            answer.extend(digits)

        return answer
        