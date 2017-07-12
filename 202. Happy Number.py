class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        transit = set()
        while True:
            if n not in transit:
                transit.add(n)
                n = sum( [int(x)*int(x) for x in list(str(n))])
                if n == 1:
                    return True 
            else:
                return False 
