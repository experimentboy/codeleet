class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        if num > 0:
            return math.log(num, 4) % 1 == 0
        else:
            return False
