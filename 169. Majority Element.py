class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        c = 1
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                c = c + 1
            else:
                c = c - 1
                if c == 0:
                    i = j
                    c = 1 
        return nums[i]
