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
        try:
            for spisok_index, spisok in enumerate(grid):
                for yacheika_index, yacheika in enumerate(spisok):
                    if yacheika == '1':
                        if spisok[yacheika_index+1] == '0' and grid[spisok_index+1][yacheika_index] == '0':
                            number_of_islands += 1
                            break
        except:
            number_of_islands += 1

        return number_of_islands


solution = Solution200()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
