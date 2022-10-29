class Solution:
    def interpret(self, command: str) -> str:
        #out = command.replace("()", "o")
        #out = out.replace("(al)", "al")
        
        
        out = ""
        k = 0
        while k < len(command):
            if command[k:k+2] == "()":
                out += "o"
                k += 2
            elif command[k:k+4] == "(al)":
                out += "al"
                k += 4
            else:
                out += command[k]
                k += 1
        
        return out