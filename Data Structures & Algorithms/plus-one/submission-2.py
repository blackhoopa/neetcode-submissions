class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        answers = []
        if digits == [9] * len(digits):
            return ([1]+[0]*len(digits))
        elif digits[-1] != 9:
            answers = digits[:-1] + [digits[-1] + 1]
            return answers
        else :
            return self.plusOne(digits[:-1]) + [0]
