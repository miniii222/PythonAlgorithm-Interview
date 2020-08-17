#https://leetcode.com/problems/3sum/
#출처 : https://github.com/onlybooks/algorithm-interview
#Solution : 두 포인터로 합 계산
def threeSum(self, nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()
    
    for i in range(len(nums)- 2) :
        
        #중복제거
        if i > 0 and nums[i] == nums[i - 1] :
            continue
        #left, right는 i 기준으로 다 오른쪽
        left, right = i + 1, len(nums) - 1
        
        while left < right :
            sum = nums[i] + nums[left] + nums[right]
            
            #sum이 0보다 작으면, left를 오른쪽으로
            #sum이 0보다 크면, right를 왼쪽으
            if sum < 0 :
                left += 1
            elif sum > 0 :
                right -= 1
            else :
                results.append([nums[i], nums[left], nums[right]])
                
                #중복제거
                while left < right and nums[left] == nums[left + 1] :
                    left += 1
                while left < right and nums[right] == nums[right - 1] :
                    right -=1
                    
                left += 1; right -= 1
                    
    return results