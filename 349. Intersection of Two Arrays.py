class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table = {}
        out = []
        for n in nums1:
            table[n] = 1
        for n in nums2:
            if n in table:
                if table[n] == 1:
                    out.append(n)
                    table[n] = 2
        return out
