"""
Time complexity: O(N)
Space complexity: O(1)
Time: 7min
Approach:
inf number of boats
each boat can carry 2 people
each boat can only carry `limit` weight

Pair the heaviest with the lightest. if the overall weight is <= limit, put both people in the boat.
Otherwise, only put the heaviest.
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        num_boats = 0
        left = 0
        right = len(people) - 1
        while left < right:
            curr_weight = people[left] + people[right]
            if curr_weight <= limit:
                num_boats += 1
                left += 1
                right -= 1
            else:
                num_boats += 1
                right -= 1
        
        # Add remaining person
        if left == right:
            num_boats += 1

        return num_boats
        