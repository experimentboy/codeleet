class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = s[::-1] 
        print(s)
        i = 1
        out = 0
        for char in s:
            temp = dict.index(char) + 1
            print(temp)
            out = out + (temp * i)
            i = i * 26
        return out
