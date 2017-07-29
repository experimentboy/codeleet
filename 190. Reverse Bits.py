class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = str("{0:b}".format(n))
        if len(b) < 32:
            b = ("0" * (32-len(b))) + b
        out = 0
        for i in range (0, len(b)):
            out = out + (int(b[i])* 2**i)
        return out
