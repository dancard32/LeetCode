class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        flip_str = ""
        
        for i in range(len(tmp)):
            flip_str += tmp[-i-1]
        
        if flip_str == tmp: return True
        else: return False
            