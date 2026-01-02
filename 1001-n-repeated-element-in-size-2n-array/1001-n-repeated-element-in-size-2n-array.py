class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_dict = dict(Counter(nums))


        for key in nums_dict:
            if nums_dict[key] == len(nums)/2:
                return key

