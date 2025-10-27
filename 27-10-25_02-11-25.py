from typing import List


# 27.10.2025
# 136 easy
class Solution136:
    def singleNumber(self, nums: List[int]):
        for i in nums:
            if nums.count(i) == 1:
                return i


# 66 easy
class Solution66:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in digits:
            digits[digits.index(int(i))] = str(i)
        number = int(''.join(digits)) + 1
        digits = []
        for i in str(number):
            digits.append(int(i))
        return digits


# 344 easy first way
class Solution344_1:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()


# second way
class Solution344_2:
    def reverseString(self, s: List[str]) -> None:
        ss = s.copy()
        for i in range(1, len(s)+1):
            s[i-1] = ss[-i]
        return s
