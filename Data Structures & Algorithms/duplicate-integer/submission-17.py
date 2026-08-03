class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Given an array of integers 'nums'
        return True if any appear more than once
        else return False

        Input: nums = [1, 2, 3, 3]

        Output: True

        Input: nums = [1, 2, 3, 4]

        Output: False

            Brute Force Approach

            Iterate over the array
            for each, iterate over the array again
            check for equality
            if yes, return True
            else if you finish the iteration
            return False


            Space: O(1)
            Time: O(n^2)

            Hashmap Approach

            Iterate over the array, create Hashmap
            check if integer already exists in hashmap,
            if yes, return True
            else create entry in hashmap, continue
            if you reach end of the array, return False

            Space: O(n)
            Time: O(n)
            """ 
        seen = {}

        for n in nums:
            if n in seen:
                return True
            else:
                seen[n] = 1
        return False
