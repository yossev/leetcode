class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = 0
        odd_cnt = 0
        even_cnt = 0
        res = 0
        MOD = 10**9 + 7

        for n in arr:
            cur_sum += n

            if cur_sum % 2:
                res += 1
                res += even_cnt
                odd_cnt+=1
            else:
                res += odd_cnt
                even_cnt += 1
        return res % MOD 



