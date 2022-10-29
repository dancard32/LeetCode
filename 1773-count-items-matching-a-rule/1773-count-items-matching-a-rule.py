class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counts = 0
        for i in range(len(items)):
            if ruleKey == "type":
                if items[i][0] == ruleValue: counts += 1
            elif ruleKey == "color":
                if items[i][1] == ruleValue: counts += 1
            elif ruleKey == "name":
                if items[i][2] == ruleValue: counts += 1
                    
        return counts