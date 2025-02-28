class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        cnt=0
        for i in nums:
            if i == val:
                nums.append(nums.pop(nums.index(i))) # Push it to the end of the array
            
        for j in nums:
            if j == val:
                j = '_'
            else:
                cnt+=1
        

        return cnt