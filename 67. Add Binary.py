class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        valA = 0
        valB =0
        for i in range (0, len(a)):
            valA = valA + (int(a[i])* 2**i)
        for i in range (0, len(b)):
            valB = valB + (int(b[i])* 2**i)
        return bin(valA+valB)[2:]
