class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for i, char in enumerate(s):
            if char == 'A' and a == 1:
                return False
            else:
                if char == 'A':
                    a+=1
            if l == 2:
                if char == 'L':
                    return False
                else:
                    l = 0
            if char == 'L':
                l += 1
            else:
                l = 0
        return True
