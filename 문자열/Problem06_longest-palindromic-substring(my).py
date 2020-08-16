#https://leetcode.com/problems/longest-palindromic-substring/

s = 'abcda'
def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]: return s
        
        answer = s[0]
        #모든 경우 다 파악.
        for i in range(len(s) - 1) :
            left = i
            right = i+1
            
            while right < len(s) :
                temp = s[left : right + 1]; temp2 = temp[::-1]
                #palindromic이 성립하고, answer보다 길 경우
                #right pointer만 이동하고, 전체를 비교. <- 메모리, 시간 소모
                if temp == temp2 and len(temp) > len(answer):
                    answer = temp

                right += 1
        return answer
