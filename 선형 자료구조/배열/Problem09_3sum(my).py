#https://leetcode.com/problems/3sum/
#시간 초과...

nums = [-1, 0, 1, 2, -1, -4]
#nums = [-2,0,1,1,2]
nums = sorted(nums)
n = len(nums)
nums
answer = []
#%%
p_index = [idx for idx, val in enumerate(nums) if val >= 0][0]  
for i in range(p_index) :
    for j in range(i + 1, n) :
        print(nums[i], nums[j])
        two_sum = nums[i] + nums[j]
        
        #둘 다 음수
        if nums[i] * nums[j] > 0 :
            new_ind = p_index
        elif nums[i] * nums[j] <= 0 :
            new_ind = j + 1
            
        if - two_sum in nums[new_ind:] :
            temp = [nums[i], nums[j], - two_sum]
            if temp not in answer : answer.append(temp)