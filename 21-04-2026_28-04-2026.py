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


# 21.04.2026
# 200 medium
class Solution200:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        for spisok_index, spisok in enumerate(grid):
            is_continue = False
            for yacheika_index, yacheika in enumerate(spisok):
                if yacheika == '1':
                    if spisok_index+1 < len(grid) and yacheika_index+1 < len(spisok):
                        if grid[spisok_index+1][yacheika_index] == '0':
                            if spisok[yacheika_index+1] == '0' and not is_continue:
                                number_of_islands += 1
                        else:
                            is_continue = True
                    else:
                        if yacheika_index+1 < len(spisok): ## проверка крайних
                            if spisok[yacheika_index+1] == '0' and not is_continue:
                                number_of_islands += 1
                        elif spisok_index+1 < len(grid): ## проверка нижних
                            if grid[spisok_index+1][yacheika_index] == '0' and not is_continue:
                                number_of_islands += 1
                        else:
                            number_of_islands += 1

        return number_of_islands
