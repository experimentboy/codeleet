class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(numbers)):
            if target - numbers[i] in h:
                return [h[target - numbers[i]]+1, i+1]
            h[numbers[i]] = i
