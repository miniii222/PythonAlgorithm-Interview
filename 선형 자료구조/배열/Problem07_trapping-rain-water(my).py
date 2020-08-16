#https://leetcode.com/problems/trapping-rain-water/
#not yet....
height = [0,1,0,2,1,0,1,3,2,1,2,1]

#%%
max_height = height.index(max(height))
left = height[:max_height + 1]; right = height[max_height]
left
