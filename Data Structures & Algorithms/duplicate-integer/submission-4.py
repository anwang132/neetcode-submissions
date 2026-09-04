class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)):
            if (len(nums) == 1):
                return False
            if (nums[i-1] == nums[i]):
                return True
        return False
            
            