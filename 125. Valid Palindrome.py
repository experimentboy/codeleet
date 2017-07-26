class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        cleanString = re.sub('\W+','', s)
        cleanString=cleanString.upper()
        if cleanString=='': return True
        if cleanString == cleanString[::-1]:
            return True
        return False
