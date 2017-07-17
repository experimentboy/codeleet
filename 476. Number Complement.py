class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        X = "{0:b}".format(num)
        Y = ""
        out = 0
        for i in range (0, len(X)):
            if X[i] == "0":
                Y = Y + "1"
            else:
                Y = Y + "0"
        Y = Y[::-1]
        for i in range (0, len(Y)):
            out= out + (int(Y[i])* 2**i)
        return out
