class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sorted_s1 = ''.join(sorted(s1))

        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False


        for i in range(len2 - len1 + 1):
            substring = s2[i:i+len1]

            if ''.join(sorted(substring)) == sorted_s1:
                return True
        return False