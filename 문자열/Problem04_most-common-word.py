#https://leetcode.com/problems/most-common-word/
#Solution : List Comprehension, Counter 객체 사용
import re
import collections

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    
    #paragraph cleansing - List Comprehension
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
                 if word not in banned]
    
    counts = collections.Counter(words) #Counter 객체
    
    #most_common 을 사용함으로써 가잔 흔하게 나타나는 값(개수 지정) return
    #내 코드와의 차이점,,
    return counts.most_common(1)[0][0]