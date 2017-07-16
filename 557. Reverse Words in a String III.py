class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s + " "
        temp = ""
        out = ""
        i = 1
        for char in s:
            if char == " " or i == (len(s)):
                out =  out + temp[::-1]
                temp = ""
                out = out + char
                i+=1
            else:
                temp += char
                i+=1
        return out[:-1]
