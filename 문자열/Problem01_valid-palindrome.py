#Solution1 : list로 변환
def isPalindrome(self, s: str) -> bool:
        strs = []
        
        for char in s :
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1 :
            #list의 pop(0)은 O(n) -> 상대적으로 느리다.
            if strs.pop(0) != strs.pop():
                return False
            
        return True


#Solution2 : deque 자료형 이용
import collections

def isPalindrome2(self, s: str) -> bool:
        strs = collections.deque()
        
        for char in s :
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1 :
            #deque에서 popleft()은 O(1) -> Solution1보다 5배 가량 빨라진다
            if strs.popleft() != strs.pop():
                return False
            
        return True
                
