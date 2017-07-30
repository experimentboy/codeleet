class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        s = sorted(nums)[::-1]
        r = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(s, r)).get, nums)
