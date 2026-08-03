"""
W: number of words
L: max length of word
Time complexity: O(W*L)
Space complexity: O(1)
Time: 20min
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compareWords(word1, word2):
            m = len(word1)
            n = len(word2)
            i = 0
            while i < min(m, n):
                if values[word1[i]] < values[word2[i]]:
                    return -1 #
                elif values[word1[i]] > values[word2[i]]:
                    return 1
                i += 1

            if i < m:
                return 1
            elif i < n:
                return -1
            return 0


        values = defaultdict(int)
        for i, char in enumerate(order):
            values[char] = i

        prev_word = words[0]
        for i in range(1, len(words)):
            curr_word = words[i]
            if compareWords(prev_word, curr_word) > 0:
                return False
            prev_word = curr_word

        return True
