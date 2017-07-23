class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # since amount of perfect numbers is extremely limited...
        perfectnumbers=[6, 28, 496, 8128, 33550336]
        if num in perfectnumbers: return True
        return False
        
