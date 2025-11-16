class Solution:
    def isHappy(self, n: int) -> bool:
        used = []
        while n not in used:
            used.append(n)
            sm = 0
            while n > 0:
                sm += (n % 10) ** 2
                n //= 10
            n = sm
            if n == 1:
                return True
        return False
