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
# 3354 easy
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        corrects = 0
        variants = []
        for index, i in enumerate(nums):
            if i == 0:
                variants.append((index, 'right'))
                variants.append((index, 'left'))
        for variant in variants:
            curr = variant[0]
            moving = variant[1]
            numes = nums.copy()
            while True:
                print(numes)
                print(variant)
                print(moving)
                print(curr)
                print('')
                if sum(numes) == 0:
                    corrects += 1
                    break
                if numes[curr] == 0:
                    if moving == 'right':
                        curr += 1
                    elif moving == 'left':
                        curr -= 1
                else:
                    if moving == 'right':
                        curr += 1
                        moving = 'left'
                    elif moving == 'left':
                        moving = 'right'
                        curr -= 1
                if curr in range(0, len(numes)):
                    if numes[curr] > 0:
                        numes[curr] -= 1

                else:
                    print(curr)
                    print(curr in range(0, len(numes) - 1))
                    print(range(0, len(numes) - 1))
                    break
        return corrects
