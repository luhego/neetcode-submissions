class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = [("", 0, 0)]
        result = []

        while combinations:
            curr_str, open_count, close_count = combinations.pop()
            if open_count == n and close_count == n:
                result.append(curr_str)

            if open_count < n:
                new_str = curr_str + "("
                combinations.append((new_str, open_count + 1, close_count))

            if open_count > close_count:
                new_str = curr_str + ")"
                combinations.append((new_str, open_count, close_count + 1))

        return result