#https://leetcode.com/problems/two-sum/
nums = [2,7,11,15]
target = 9
#%%
#Brute - Force
#최악의 풀이. 비효율적. O(n^2)
def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n) :
            for j in range(1, n - i) :
                if target == nums[i] + nums[i+j] :
                    return [i, i + j]
#%%
#in을 이용.
#똑같이 O(n^2)이지만, in은 굉장히 빠르게 동작.
def twoSum2(self, nums: list[int], target: int) -> list[int]:
    for idx, val in enumerate(nums) :
        myval = target - val
        #myval이 있는지 확인.
        if myval in nums[idx+1:] :
            return [idx, nums[idx+1:].index(myval) + len(nums[:idx+1])]
