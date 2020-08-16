#https://leetcode.com/problems/two-sum/
#출처 : https://github.com/onlybooks/algorithm-interview

#Solution : dict를 이용하여 키 조회
def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        
        for i, num in enumerate(nums) :
            if target - num in nums_map :
                return [nums_map[target - num], i]
            
            #index -> value / num -> key
            nums_map[num] = i
