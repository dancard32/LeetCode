class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()

        if len(cost) == 2: return sum(cost)

        spent = 0; k = 0; freeCandy = 0
        while True:
            if k > len(cost)-1: break
            if freeCandy == 2: 
                freeCandy = 0
                k += 1
            else: 
                spent += cost[k]

                k += 1
                freeCandy += 1

        return spent