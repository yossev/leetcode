class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        ans = n

        for i in range(0, n):
            for j in range(0, n):
                if(fruits[i]<=baskets[j]):
                    ans -= 1
                    baskets[j]=0  # Make it unusable anymore
                    break
        
        return ans
