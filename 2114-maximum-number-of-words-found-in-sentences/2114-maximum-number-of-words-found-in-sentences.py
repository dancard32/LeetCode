class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:        
        max_word = 0
        for sentence in sentences:
            tmp = len(sentence.split(" "))
            if tmp > max_word: max_word = tmp
            
        return max_word
            