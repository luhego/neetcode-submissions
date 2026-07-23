"""
Time complexity: O(N)
Space complexity: O(N)
Time: 17min

Approach:
There is only a collision when:
    - stack is not empty
    - incoming asteroid direction is negative
    - current asteroid in the stack is positive
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] > abs(asteroid):
                    asteroid = 0
                else:
                    stack.pop()
                    asteroid = 0
            
            if asteroid != 0:
                stack.append(asteroid)
        
        return stack
