class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers) - 1
        solution = []
        while i1 < i2:
            if numbers[i1] + numbers[i2] > target:
                i2 -= 1
            if numbers[i1] + numbers[i2] < target:
                i1 += 1
            if numbers[i1] + numbers[i2] == target:
                return [i1+1, i2+1]
        return []