#https://leetcode.com/problems/longest-palindromic-substring/
#출처 : https://github.com/onlybooks/algorithm-interview
def longestPalindrome(self, s: str) -> str:
    #반복적으로 수행하는 작업을 expand 메소드로 정의
    def expand(left : int, right : int) -> str :
        while left >=0 and right <= len(s) and s[left] == s[right - 1] :
            left -= 1
            right += 1

        return s[left + 1 : right - 1]

    if len(s) < 2 or s == s[::-1] :
        return s
    
    result = ''
    for i in range(len(s) - 1) :
        #이런 코드를 짜는 날이 올까...?
        result = max(result, 
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key = len)
    return result