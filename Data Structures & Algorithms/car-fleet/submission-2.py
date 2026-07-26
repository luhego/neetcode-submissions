"""
Time complexity: O(NlogN)
Space complexity: O(1)
Time: 20min

Intuition:
Starting from the last car. We can compute the time it takes
to arrive at the target.

For every new car, if its time is lower that the curr car, they will form a fleet.

So, we can use a stack to keep track of the current fleets.
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))

        # Sort cars by position(closer to target)
        combined.sort(key=lambda c: -c[0])

        stack = []
        for pos, sp in combined:
            curr_time = (target - pos) / sp
            if not stack or curr_time> stack[-1]:
                stack.append(curr_time)
        return len(stack)
