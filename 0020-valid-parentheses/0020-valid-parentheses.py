class Solution:
    def isValid(self, s: str) -> bool:
        output = []
        open_paren = {")":"(", "}":"{", "]":"["}
        
        for paren in s:
            if paren in open_paren.values():
                output.append(paren)
            elif output and open_paren[paren] == output[-1]:
                output.pop()
            else:
                return False
        return output == []