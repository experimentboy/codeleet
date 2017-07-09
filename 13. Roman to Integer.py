class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        index=0;num=0;temp=0
        while index < len(s):
            c = s[index];index+=1
            if c == 'I':num+=1;temp=1
            elif c == 'V':num+=3 if temp==1 else 5
            elif c == 'X':num+=8 if temp==1 else 10;temp=10
            elif c == 'L':num+=30 if temp==10 else 50
            elif c == 'C':num+=80 if temp==10 else 100;temp=100
            elif c == 'D':num+=300 if temp==100 else 500
            elif c == 'M':num+=800 if temp==100 else 1000
        return num
