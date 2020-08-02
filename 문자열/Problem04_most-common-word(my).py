#https://leetcode.com/problems/most-common-word/
import re
import collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    
    #paragraph cleansing
    paragraph = re.sub(pattern = '[^\w\s]',  repl = ' ', string = paragraph).lower().split()
    paragraph = [pp for pp in paragraph if pp not in banned]

    para_c = collections.Counter(paragraph)

    vv = 0; answer = ""
    for key, value in para_c.items() :
        if value > vv :
            vv = value
            answer = key
        
    return answer