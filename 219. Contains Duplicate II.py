class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pointers = {}
        for i,number in enumerate(nums):
            if number not in pointers:
                pointers[number] = [i]
            else:
                for j in pointers[number]:
                    if abs(i-j)<=k: return True
                pointers[number].append(i)
        return False
