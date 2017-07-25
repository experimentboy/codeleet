class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = []
        while n > 0:
            out.append((n-1)%26)
            n = (n-1)/26
        return ''.join(chr(i+ord('A')) for i in out[::-1])
