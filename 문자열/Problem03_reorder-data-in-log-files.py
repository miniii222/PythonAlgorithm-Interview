#https://leetcode.com/problems/reorder-data-in-log-files/
#출처 : https://github.com/onlybooks/algorithm-interview
# Solution : 람다와 +연산자를 이용
# 아이디어는 나와 동일. 좀 더 정돈된 코드

def reorderLogFiles(self, logs: list[str]) -> list[str]:
    
    dig = []; let = []
    
    for log in logs :
        if log.split()[1].isdigit() :
            dig.append(log)
        else :
            let.append(log)
    
    #내 코드와의 차이점 : 이런식으로 sort에 여러 개의 조건을 걸어줄 수 있음..
    let.sort(key = lambda x : (x.split()[1:], x.split()[0]))
    
    return let + dig