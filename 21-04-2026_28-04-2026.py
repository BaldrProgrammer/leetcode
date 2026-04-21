from typing import List


# 21.04.2026
# 27 easy
class Solution27:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)


# 21.04.2026
# 35 easy
class Solution35:
    def searchInsert(self, nums: List[int], target: int) -> int:
        set(nums)
        nums.append(target)
        return sorted(nums).index(target)


# 21.04.2026
# 58 easy
class Solution58:
    def lengthOfLastWord(self, s: str):
        return len(s.strip().split(' ')[-1])
