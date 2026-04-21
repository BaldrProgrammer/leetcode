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
# 200 medium(hard)
class Solution200:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands
