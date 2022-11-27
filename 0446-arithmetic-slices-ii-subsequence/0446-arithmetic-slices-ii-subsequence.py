class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        count = [defaultdict(int) for _ in range(length)]
        
        subseq = 0
        for i,a in enumerate(nums):
            for j,b in enumerate(nums[:i]):
                count[i][a-b] += count[j][a-b] + 1
                subseq += count[j][a-b]
        
        return subseq
        
        