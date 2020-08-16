#https://leetcode.com/problems/3sum/
#시간 초과...
nums = [-1, 0, 1, 2, -1, -4]
#%%
answer = []
n = len(nums)
for i in range(n - 1) :
    for j in range(1, n - i) :
        two_sum = nums[i] + nums[i + j]
            
        if -two_sum in nums[i + j + 1 :]:
            temp = sorted([nums[i], nums[i + j], - two_sum])
            if temp not in answer : answer.append(temp)

