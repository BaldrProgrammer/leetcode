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
    def titleToNumber171(self, col: str) -> int:
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
        for i in range(len(col) - 1):
            output += 26 * letters[col[i]] * (i+1)
        output += letters[col[-1]]
        return output

