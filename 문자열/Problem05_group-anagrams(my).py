#https://leetcode.com/problems/group-anagrams/

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    sorted_strs = []

    #모든 값 정렬  
    for ss in strs :
        sorted_strs.append(''.join(sorted(ss)))
    
    #set기준으로 리스트의 인덱스 저장
    mydict = {ss : [] for ss in set(sorted_strs)}
    for idx, ss in enumerate(sorted_strs) :
        mydict[ss].append(idx)

    answer = []
    for val in mydict.values() :
        answer.append([strs[v] for v in val])
            
    return answer