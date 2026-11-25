class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(nums[len(nums) - i - 1] * suffix[-1])
        suffix.reverse()

        result.append(suffix[1])

        for i in range(1, len(nums) - 1):
            result.append(prefix[i - 1] * suffix[i + 1])

        result.append(prefix[-2])

        return result