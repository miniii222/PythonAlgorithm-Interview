#https://leetcode.com/problems/valid-palindrome/
#best
def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        my = ""
        
        for ss in s :
            #isalnlum() -> alphabet과 숫자만 필터
            if ss.isalnum() :
                my += ss
                
        return my == my[::-1] #문자열에서 slicing 방법은 굉장히 빠른 알고리즘!