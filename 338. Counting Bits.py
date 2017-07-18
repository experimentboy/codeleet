class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        out = []
        temp = int(0)
        for i in range (num+1):
            X = "{0:b}".format(i)
            for j in range (0, len(X)):
                if X[j] == "1":
                    temp+=1
            out.append(temp)
            temp = int(0)
        return out
