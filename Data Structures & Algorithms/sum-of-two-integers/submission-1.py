class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & MASK
            b = tmp & MASK

        return a if a <= MAX_INT else a - (MASK + 1)