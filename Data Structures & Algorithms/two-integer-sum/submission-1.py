class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        two_map = {}

        for i in range(len(nums)): 
            search = target - nums[i]
            if search in two_map: 
                return [two_map[search], i]
            
            two_map[nums[i]] = i


