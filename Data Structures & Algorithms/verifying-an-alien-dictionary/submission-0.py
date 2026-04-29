class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(word_1, word_2):
            i = 0
            while i < len(word_1) and i < len(word_2):
                char_1, char_2 = word_1[i], word_2[i]
                if rank[char_1] < rank[char_2]:
                    return -1
                elif rank[char_1] > rank[char_2]:
                    return 1
                i += 1
            
            if len(word_1) == len(word_2):
                return 0
            else:
                return -1 if len(word_1) < len(word_2) else 1

        rank = {order[i]: i for i in range(len(order))}

        for i in range(1, len(words)):
            result = compare(words[i - 1], words[i])
            if result == 1:
                return False
        return True
