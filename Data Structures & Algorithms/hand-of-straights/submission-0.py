class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        freqs = defaultdict(int)
        for val in hand:
            freqs[val] += 1

        vals = sorted(list(freqs.keys()))
        for val in vals:
            if freqs[val] == 0:
                continue

            while freqs[val] > 0:
                for v in range(val, val + groupSize):
                    if freqs[v] == 0:
                        return False
                    freqs[v] -= 1

        return True
      