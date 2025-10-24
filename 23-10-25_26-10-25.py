from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 22.10.2025
# 1342 easy
class Solution1342:
    def numberOfSteps(self, n: int) -> int:
        count = 0
        while n > 0:
            if n % 2 == 0:
                n /= 2
            else:
                n -= 1
            count += 1
        return count


# 412 easy
class Solution412:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n + 1):
            if int(i) % 3 == 0 and int(i) % 5 == 0:
                output.append('FizzBuzz')
                continue
            elif int(i) % 3 == 0:
                output.append('Fizz')
            elif int(i) % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output


# 876 easy
class Solution876:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        output = []
        count = 0
        while a.next:
            count += 1
            a = a.next
        half_count = int((count + 1) / 2) + 1

        a = head
        for i in range(half_count - 1):
            a = a.next
        while a:
            output.append(a.val)
            a = a.next
        fjaklesd = []
        for index, i in enumerate(reversed(output)):
            if index >= 1:
                a = ListNode(i, fjaklesd[index - 1])
            else:
                a = ListNode(i)
            fjaklesd.append(a)
        return a


# 23.10.2025
# 383 easy
class Solution383:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = list(ransomNote)
        for i in magazine:
            if i in letters:
                letters.remove(i)
        if letters:
            return False
        else:
            return True


# 3461 easy
class Solution3461:
    def hasSameDigits(self, s: str) -> bool:
        new_digit = ''
        while True:
            for i in range(len(s) - 1):
                new_digit += str((int(s[i]) + int(s[i + 1])) % 10)
            if len(new_digit) == 2:
                break
            else:
                s = new_digit
                new_digit = ''

        if int(new_digit[0]) == int(new_digit[1]):
            return True
        else:
            return False


# 24.10.2025
# 2048 medium first way
class Solution:
    def nextBeautifulNumber(self, n: int):
        nums = [1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 22333, 23233, 23323, 23332, 32233,
                32323, 32332, 33223, 33232, 33322, 41444, 44144, 44414, 44441, 55555, 122333, 123233, 123323, 123332,
                132233, 132323, 132332, 133223, 133232, 133322, 155555, 212333, 213233, 213323, 213332, 221333, 223133,
                223313, 223331, 224444, 231233, 231323, 231332, 232133, 232313, 232331, 233123, 233132, 233213, 233231,
                233312, 233321, 242444, 244244, 244424, 244442, 312233, 312323, 312332, 313223, 313232, 313322, 321233,
                321323, 321332, 322133, 322313, 322331, 323123, 323132, 323213, 323231, 323312, 323321, 331223, 331232,
                331322, 332123, 332132, 332213, 332231, 332312, 332321, 333122, 333212, 333221, 422444, 424244, 424424,
                424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 555551, 666666,
                1224444]
        for i in nums:
            if n < i:
                return i


# second way
class Solution2048:
    def nextBeautifulNumber(self, n: int):
        for i in range(n + 1, 9909999):
            nums = set(str(i))
            sovpadenie = 0
            for ii in nums:
                if str(i).count(ii) == int(ii):
                    sovpadenie += 1
                    print(ii, str(i).count(ii))
                else:
                    continue
                print(i, sovpadenie)
                print('')

            if sovpadenie == len(nums):
                return i


# 25.10.2025
# 1 easy first way
class Solution1:
    def twoSum(self, nums: List[int], target: int):
        for index, i in enumerate(nums):
            nums2 = nums.copy()
            nums2.pop(index)
            for iindex, ii in enumerate(nums2):
                if i + ii == target:
                    return [index, iindex + 1]
