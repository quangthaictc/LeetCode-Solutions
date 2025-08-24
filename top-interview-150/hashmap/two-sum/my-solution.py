class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            
            needToFind = target - num

            if needToFind in map:
                return sorted([i, map[needToFind]])

            map[nums[i]] = i
        return []

"""
It all means the following:
    - Variable 'map' stores index of visited values ​​in a list
    - Loop 'nums' list
    - [target] = two numbers in the list added together => [needToFind] = [target] - [value of list index]
    - For each value in list, check visited values if 'needToFind' already exist => return two index
"""

