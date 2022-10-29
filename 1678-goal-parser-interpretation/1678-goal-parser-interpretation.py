class Solution:
    def interpret(self, command: str) -> str:
        out = command.replace("()", "o")
        out = out.replace("(al)", "al")
        
        return out