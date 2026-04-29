class Solution:
    def reverse(self, x: int) -> int:
        multiplier = -1 if x < 0 else 1
        x = abs(x)

        lower_bound = -2 ** 31
        upper_bound = 2 ** 31 - 1

        reverse_x = 0
        while x > 0:
            digit = x % 10
            x //= 10

            reverse_x = reverse_x * 10 + digit
            if multiplier == -1 and reverse_x < lower_bound or reverse_x > upper_bound:
                return 0

        return multiplier * reverse_x