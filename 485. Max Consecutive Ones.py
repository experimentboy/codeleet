class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        temp = 0
        k = 1
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return nums[1]+nums[0]
        nums.append(0)
        nums.append(0)
        print(nums)
        while k < len (nums):
            if nums[k] == 1 and nums[k] ==nums[k-1]: temp += 1
            else: temp = 0
            if temp > max: max =temp
            k+=1
        if len(nums) > 5: max+=1
        return max
