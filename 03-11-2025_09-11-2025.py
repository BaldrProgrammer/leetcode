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
