class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num+=1
        digits_array = [int(digit) for digit in str(num)]
        return digits_array
