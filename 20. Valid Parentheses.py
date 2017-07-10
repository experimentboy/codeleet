class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def pair(a,b):
            if (a == "(" and b == ")") or (a == "{" and b == "}") or (a == "[" and b == "]"):
                return True
            else:
                return False
        transit = []
        for i in range(len(s)):
            if (s[i] == "(" or s[i] == "{" or s[i] == "["):
                transit.append(s[i])
            elif not transit:
                return False
            else:
                c = transit.pop()
                if not pair(c,s[i]):
                    return False
        if transit:
            return False
        else:
            return True
