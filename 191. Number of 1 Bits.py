class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        b = str("{0:b}".format(n))
        index = 0
        while index < len(b):
            if b[index] == '1': out += 1
            index += 1
        return out
