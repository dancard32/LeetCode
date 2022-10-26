class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.countCharsInString(s) == self.countCharsInString(t)

    def countCharsInString(self, s):
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts
