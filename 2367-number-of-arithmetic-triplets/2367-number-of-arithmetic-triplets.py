class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        len_nums = len(nums)
        counts = 0
        
        for i in range(len_nums):
            for j in range(i, len_nums):
                for k in range(j, len_nums):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff and i < j < k:
                        counts += 1
        return counts