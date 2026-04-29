class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert to binary, remove the first two values(0b), reverse it and convert it back to int
        return int(bin(n)[2:].zfill(32)[::-1], 2)