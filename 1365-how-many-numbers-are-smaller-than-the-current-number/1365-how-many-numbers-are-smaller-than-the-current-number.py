class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j] and i != j:
                    counts[i] += 1
                    
        return counts