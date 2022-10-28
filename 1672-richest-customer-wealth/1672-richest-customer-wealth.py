class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            sum_acc = sum(account)
            if sum_acc > max_wealth: max_wealth = sum_acc
                
        return max_wealth