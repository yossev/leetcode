class Solution(object):

    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        store_pairs=[]


        for i in range(len(nums)):
            number = str(nums[i])
            formed = ""
            for j in range(len(number)):
                formed+= str(mapping[int(number[j])])
            mapped_value = int(formed)
            store_pairs.append((mapped_value, i))
        
        store_pairs.sort()
        answer = []
        for pair in store_pairs:
            # Only Append Original Values
            answer.append(nums[pair[1]])

        return answer
