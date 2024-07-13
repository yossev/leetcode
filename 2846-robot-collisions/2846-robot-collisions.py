class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        stack = deque()
        n = len(positions)
        indices = list(range(n))
        result = []

        indices.sort(key=lambda x: positions[x])

        for curr_index in indices:
            if directions[curr_index] == "R":
                stack.append(curr_index)
            else:
                while stack and healths[curr_index] > 0:
                    # Most recent right direction
                    top_index = stack.pop()
                    if healths[top_index] > healths[curr_index]:
                        healths[top_index] -= 1
                        healths[curr_index] = 0 # Kill curr index
                        stack.append(top_index)
                    elif healths[top_index] < healths[curr_index]:
                        healths[top_index] = 0
                        healths[curr_index] -= 1 
                    else:
                        healths[top_index] = 0
                        healths[curr_index] = 0

        for index in range(n):
            if healths[index] > 0:
                result.append(healths[index])


        return result