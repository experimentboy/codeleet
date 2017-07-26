class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        def xrange(x):return iter(range(x))
        for a in xrange(int(math.sqrt(c))+1):
            b = int(math.sqrt(c-a**2))
            if a**2 + b**2 == c:
                return True
        return False
