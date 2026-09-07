class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        con = 0
        for i in num_set:
            if i - 1 in num_set:
                continue
            length = 0
            while i + length in num_set:
                length += 1
            con = max(con, length)
        return con


