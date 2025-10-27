from typing import List

# 27.10.2025
# 136 easy
class Solution136:
    def singleNumber(self, nums: List[int]):
        for i in nums:
            if nums.count(i) == 1:
                return i



