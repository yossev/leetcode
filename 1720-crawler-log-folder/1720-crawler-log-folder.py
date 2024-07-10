class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        counter = 0

        for log in logs:
            if log == "../":
                if counter > 0:
                    counter-=1
            elif log == "./":
                continue
            else:
                counter+=1
        return counter