class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for n in range(1, len(nums)):
            if (nums[n] == nums[n-1]):
                return True
        return False