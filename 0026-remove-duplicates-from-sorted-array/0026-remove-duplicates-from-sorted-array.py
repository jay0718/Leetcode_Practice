class Solution(object):
    def removeDuplicates(self, nums):
        j = 0
        for i in nums:
            if i not in nums[:j]:
                nums[j]=i
                j += 1
        return j
        