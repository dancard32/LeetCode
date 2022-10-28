class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return address.replace(".", "[.]")
        
        tmp = ""
        for i in address:
            if i == ".":
                tmp += "[.]"
            else:
                tmp += i
        return tmp