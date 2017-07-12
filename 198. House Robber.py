class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        transit = [0]*n
        transit[0] = nums[0]
        transit[1] = nums[1]
        transit[2] = nums[2] + nums[0]
        for i in range(3,n):
            transit[i] = max(transit[i-2], transit[i-3])+ nums[i]
        return max(transit[-1], transit[-2])
