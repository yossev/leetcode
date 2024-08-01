class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curralt = 0
        maxalt=curralt

        for alt in gain:
            curralt+=alt
            maxalt=max(maxalt, curralt)
        return maxalt