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


# 7 medium
class Solution7:
    def reverse(self, x: int) -> int:
        xx = x
        if x < 0:
            xx = abs(x)
        hui = list(str(xx))
        hui.reverse()
        result = int(''.join(hui))
        if -2**31 <= result <= 2**31 - 1:
            if x < 0:
                return result - result - result
            else:
                return result
        else:
            return 0


# 28.10.2025
# 3354 easy NOT MINE
class Solution3354(object):
    def countValidSelections(self, nums):
        total, ls, cases = sum(nums), 0, 0
        for i in range(len(nums)):
            rs = total - ls - nums[i]
            if nums[i] == 0:
                if ls == rs:
                    cases += 2
                elif ls == rs - 1 or ls - 1 == rs:
                    cases += 1
            ls += nums[i]
        return cases
