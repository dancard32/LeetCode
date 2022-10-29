class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        out = ["" for na in range(len(indices))]
        
        k = 0
        for ind in indices:
            out[ind] = s[k]
            k += 1
            
        str_out = ""
        for i in range(len(indices)): str_out += out[i]
            
        return str_out