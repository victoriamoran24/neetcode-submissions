class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        starters = []

        if nums == []:
            return 0


        for n in nums: 
            if n+1 in nums_set and n-1 not in nums_set: 
                starters.append(n)

        counter_max = 1

        for s in starters: 
            counter = 1
            while s + 1 in nums_set: 
                counter += 1
                s += 1
            counter_max = max(counter_max, counter)

        return counter_max


