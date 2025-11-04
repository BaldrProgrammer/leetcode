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
