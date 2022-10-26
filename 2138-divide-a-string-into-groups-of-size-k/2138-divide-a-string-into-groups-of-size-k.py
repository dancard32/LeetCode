class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []
        for i in range(0, len(s), k):
            output.append(s[i:i+k])
        output[len(output)-1] += (k - len(output[len(output)-1]))*fill

        return output