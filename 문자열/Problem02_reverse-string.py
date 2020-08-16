#https://leetcode.com/problems/reverse-string/
#출처 : https://github.com/onlybooks/algorithm-interview
#Solution1 : 두개의 포인터를 이용한 스왑(전통적인 방식)
def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right :
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        
#Solution2 : Pythonic way
def reverseString2(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse() #값을 return하지 않고, s자체를 바꿈