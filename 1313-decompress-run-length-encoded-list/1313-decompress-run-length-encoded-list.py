class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i in range(0, len(nums), 2):
            for na in range(nums[i]):
                ans.append(nums[i+1])
        return ans