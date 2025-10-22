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
        for i in range(1, n+1):
            if int(i)%3 == 0 and int(i)%5 == 0:
                output.append('FizzBuzz')
                continue
            elif int(i)%3 == 0:
                output.append('Fizz')
            elif int(i)%5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output

# 876 easy
