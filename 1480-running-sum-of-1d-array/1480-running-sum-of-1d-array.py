class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
                
        #return [sum(nums[:i]) for i in range(1,len(nums)+1)]
        import numpy as np

        ans = np.array(nums)
        for i in range(1, len(nums)):
            ans[i:]+= nums[i-1]
            
        return ans