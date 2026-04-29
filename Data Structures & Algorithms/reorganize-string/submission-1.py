from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = defaultdict(int)
        for char in s:
            freqs[char] += 1

        max_heap = []
        for char, freq in freqs.items():
            heappush(max_heap, (-freq, char))

        answer = []
        while len(max_heap) > 0:
            freq, char = heappop(max_heap)

            if len(answer) == 0 or answer[-1] != char:
                answer.append(char)

                freq += 1
                if freq != 0:
                    heappush(max_heap, (freq, char))
            else:
                # Heap is empty so there is no other character to use
                if len(max_heap) == 0:
                    return ""
    
                next_freq, next_char = heappop(max_heap)
                answer.append(next_char)

                next_freq += 1
                if next_freq != 0:
                    heappush(max_heap, (next_freq, next_char))

                heappush(max_heap, (freq, char))
        
        return "".join(answer)
