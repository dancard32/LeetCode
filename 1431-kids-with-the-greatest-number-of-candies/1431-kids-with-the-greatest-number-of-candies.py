class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in range(len(candies)):
            if i == 0:
                if candies[i]+extraCandies >= max(candies[i:]):
                    ans.append(True)
                else:
                    ans.append(False)
            elif i == len(candies)-1:
                if max(candies[:i]) <= candies[i]+extraCandies:
                    ans.append(True)
                else:
                    ans.append(False)
            elif max(candies[:i]) <= candies[i]+extraCandies >= max(candies[i:]):
                ans.append(True)
            else: ans.append(False)
                
        return ans