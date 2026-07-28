class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two Sum

        Given an array of integers and a target k
        return the indices i and j such that nums[i] +
        nums[j] = k

        you can assume that every input contains exactly
        one pair that adds to k

        return the answer with the smaller index first

        input
        nums = [3, 4, 5, 6], k = 7

        output: [0, 1]


        Brute Force

        iterate over nums
        subtract current from target
        search in array for result
        return current and result
        otherwise continue looping

        time = iterating over the array, searching in the array (same thing? just twice potentially)

        space = constant I think, 
        you're not creating another data structure


        Hashmap Approach

        iterate over array
        create hashmap where key is the number
        and value is the index of that number in the array

        iterate over keys in hashmap
        check if target - current is in the keys
        if yes
        return values (indices)
        else continue


        time = iterating over the array
        iterating over hashmap

        space = creating a hashmap



        """


        indexmap = {}

        for i in range(len(nums)):
            print(f"current  index i {i}")
            complement = target - nums[i]
            print(f"current complement {complement}")
            if complement in indexmap:
                return [indexmap[complement], i ]
            indexmap[nums[i]] = i
            print(indexmap)


        


                