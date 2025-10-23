# 23.10.2025
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

