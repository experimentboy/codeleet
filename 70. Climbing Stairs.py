class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        out = [0] * (n + 1)
        out[0] = 1
        out[1] = 1
        for i in range(2, n + 1):
            out[i] = out[i - 1] + out[i - 2]
        return out[n]
