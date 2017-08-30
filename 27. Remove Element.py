class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            num = nums[i]
            if num != val:
                nums[index] = num
                index += 1
        return index   
