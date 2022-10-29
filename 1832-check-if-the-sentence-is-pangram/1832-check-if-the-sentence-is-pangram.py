class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if sentence.isdigit(): return False
        elif len(set(sentence.lower())) == 26: return True
