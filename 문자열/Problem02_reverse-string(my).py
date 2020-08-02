#https://leetcode.com/problems/reverse-string/
def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        #s = s[::-1] 원래 작동하는 코드인데, 리트코드에서는 변수 할당을 처리하는데 제약이 있음;