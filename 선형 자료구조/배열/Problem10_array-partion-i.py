#https://leetcode.com/problems/array-partition-i/
#출처 : https://github.com/onlybooks/algorithm-interview
#Solution : Pythonic Code
def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])
