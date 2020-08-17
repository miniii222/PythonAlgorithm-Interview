#https://leetcode.com/problems/array-partition-i/

nums = [1,4,3,2]
nums = [1,2,4,7,9,11]
#%%
nums.sort()
#생각해보면 결과적으로 정렬 후, 홀수번째 만 pick
[num for i, num in enumerate(nums) if i%2 == 0]