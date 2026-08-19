class Solution:
    def sumofSquare(self, n: int) -> int:
        output = 0
        while n:
            dig = n % 10
            output+= dig ** 2
            n = n//10
        return output

    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumofSquare(n)
            if n == 1:
                return True
        return False
