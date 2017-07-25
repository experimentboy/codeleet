class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 9
        cnt = 1
        while n > num * cnt:
            n -= (num * cnt)
            num *= 10
            cnt += 1
        t = n // cnt
        base = 10 ** (cnt - 1) + t
        if t * cnt == n: return (base - 1) % 10
        n -= t * cnt
        return int(str(base)[::-1][-n])
