class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        res=0

        for person in details:
            age = int(person[11:13])
            if age > 60:
                res+=1
        return res