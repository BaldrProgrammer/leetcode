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
        for i in range(1, len(s) + 1):
            s[i - 1] = ss[-i]
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
        if -2 ** 31 <= result <= 2 ** 31 - 1:
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


# 29.10.2025
# 3370 easy first way
class Solution3370_1:
    def smallestNumber(self, n: int):
        for i in range(n, 1000):
            if '0' not in str(bin(i)).replace('0b', ''):
                return i


# second way
class Solution3370_2:
    def smallestNumber(self, n: int):
        outputs = [
            1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047,
        ]
        for i in outputs:
            if i >= n:
                return i


# 189 medium
class Solution189:
    def rotate(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        while k > len(nums):
            if len(nums) > 1:
                k //= len(nums)
            else:
                k //= 2
        new_list = nums[-k:]
        print(nums[-k])
        new_list += nums[0:len(nums) - k]
        for index, i in enumerate(new_list):
            nums[index] = i
        print(nums)


# 283 easy
class Solution283:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)


# 350 easy
class Solution350:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            if num in nums2:
                nums2.remove(num)
                output.append(num)
        return output


# 02.11.2025
# 242 easy first way
class Solution242:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            t = list(t)
            for i in s:
                if i in t:
                    t.remove(i)
            if t != []:
                return False
            else:
                return True
        else:
            return False


# 14 easy
class Solution14:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        for letter in max(strs):
            for i in strs:
                if not i.startswith(prefix):
                    print(prefix)
                    return prefix[:-1]
            prefix += letter

        for i in strs:
            if not i.startswith(prefix):
                print(prefix)
                return prefix[:-1]

        return prefix

# 28 easy
class Solution28:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1
