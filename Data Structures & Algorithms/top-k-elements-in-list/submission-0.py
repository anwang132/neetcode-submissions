class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums).most_common(k) 
        y = []
        y.extend(item[0] for item in x)
        return y
            