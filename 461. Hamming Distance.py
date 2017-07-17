class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        X = "{0:b}".format(x)
        Y = "{0:b}".format(y)
        X = X[::-1]
        Y = Y[::-1]
        if len(X) < len(Y):
            fill = len(Y) - len(X)
            for i in range (0, fill):
                X = X + "0"
        else:
            fill = len(X) - len(Y)
            for i in range (0, fill):
                Y = Y + "0"
        out = 0
        print(X,Y)
        for i in range (0, len(X)):
            if X[i] != Y[i]:
               out+=1  
        return out
