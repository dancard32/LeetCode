class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sums = 0
        for digit in str(n):
            prod *= int(digit)
            sums += int(digit)
            
        return prod - sums