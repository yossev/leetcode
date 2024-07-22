class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = list(zip(heights, names))
        people.sort(reverse=True, key=lambda x: x[0])

        res = [name for _, name in people]

        return res

