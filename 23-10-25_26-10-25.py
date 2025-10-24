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
# 2048 medium
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

