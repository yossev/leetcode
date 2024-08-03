class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        target.sort()

        for i in range(len(arr)):
            if arr[i] != target[i]:
                return False
        return True