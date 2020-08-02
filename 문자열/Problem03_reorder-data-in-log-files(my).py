#https://leetcode.com/problems/reorder-data-in-log-files/

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]


def reorderLogFiles(self, logs: list[str]) -> list[str]:
    dig = []; let = []
    # dig, let 분리
    for ll in logs :
        #try보다는, "234".isdiit()을 하면 ture or false 알 수 있음
        try :
            int(ll.split()[1])
            dig.append(ll)
        except ValueError :
            let.append(ll)
    # let 알파벳 순      
    let.sort(key = lambda x : x.split()[0])
    let.sort(key = lambda x : x.split()[1:])
        
    #dig는 그대로 맨 뒤에
    return let + dig
