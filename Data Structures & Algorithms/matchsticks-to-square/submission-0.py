class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def backtrack(i):
            if i == n:
                return all(side_len == S for side_len in sides)

            # Each stick can be assigned to any side for only one of them
            for s in range(4):
                # Can't place stick i in side s
                if sides[s] + matchsticks[i] > S:
                    continue
                
                # Put stick i in side s
                sides[s] += matchsticks[i]
                result = backtrack(i + 1)

                # Remove stick i from side s
                sides[s] -= matchsticks[i]

                if result:
                    return True

            return False


        P = sum(matchsticks)
        if P % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        S = P // 4
        n  = len(matchsticks)
        sides = [0] * 4
        return backtrack(0)