from typing import List

# 03.11.2025
# 387 easy
class Solution387:
    def firstUniqChar(self, s: str) -> int:
        indexes = []
        for i in set(s):
            if s.count(i) == 1:
                indexes.append(s.index(i))
        if indexes:
            return min(indexes)
        return -1

# 04.11.2025
# 169 easy
class Solution169:
    def majorityElement(self, nums: List[int]):
        for i in set(nums):
            if nums.count(i) > len(nums)/2:
                return i


# 171 easy
class Solution:
    def titleToNumber(self, col: str) -> int:
        letters = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26
        }
        output = 0
        ite = list(range(len(col)))[::-1]
        for i in ite:
            print(i)
            output += letters[col[ite.index(i)]] * (26 ** i)
        return output


# 69 easy first way
class Solution69:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)


# 125 easy
class Solution125:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i in 'abcdefghijklmnopqrstuvwxyz0123456789']
        if s == s[::-1]:
            return True
        return False