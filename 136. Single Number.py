class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        for n in nums:
            out ^=n
        return out
