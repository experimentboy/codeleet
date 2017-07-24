class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        down=0
        up=len(nums)
        while down < up :
            mid = (down+up)>>1
            if nums[mid] < target:
                down =mid + 1
            else:
                up = mid
        return down
