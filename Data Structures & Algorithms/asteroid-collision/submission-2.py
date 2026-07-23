"""
Time complexity: O(N)
Space complexity: O(N)
Time: 17min
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid >= 0 or not stack:
                stack.append(asteroid)
            else:
                pos_asteroid = abs(asteroid)
                destroyed = False
                while stack and not destroyed:
                    top = stack[-1]
                    if top < 0:
                        break
                    elif top == pos_asteroid:
                        # both asteroids destroyed
                        stack.pop()
                        destroyed = True
                    elif top > pos_asteroid:
                        # incoming asteroid destroyed
                        destroyed = True
                    else:
                        # current asteroid destroyed
                        stack.pop()
                
                if not destroyed:
                    stack.append(asteroid)
        
        return stack
