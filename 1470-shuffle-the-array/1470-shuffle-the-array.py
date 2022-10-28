class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = nums
        # [2, 5, 1, 3, 4, 7]
        #  0. 1. 2. 3  4. 5
        
        
        # [2, 3, 1, 5, 4, 7]
        # indices 1, 3 flip
        
        # [2, 3, 4, 5, 1, 7]
        # indices 2, 4 flip
        """
        print(ans)
        for i in range(1, n):
            xn = nums[i]
            yn = nums[i+n-1]
            ans[i] = yn
            ans[i+n-1] = xn
            
            print(ans)
        """
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        
        return ans