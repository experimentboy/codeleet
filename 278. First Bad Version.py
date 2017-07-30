# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        up=1
        down=n
        while up <= down:
            mid = (up + down) / 2
            if isBadVersion(mid):
                down = mid - 1
            else:
                up = mid + 1
        return up
