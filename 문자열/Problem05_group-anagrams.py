#https://leetcode.com/problems/group-anagrams/
import collections
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #빈 dict 선언
    anagrams = collections.defaultdict(list)
    
    for word in strs :
        #나처럼 index를 가져와서 다시 값을 가져오는 것이 아니라
        #처음부터 값을 dict에 저장
        anagrams[''.join(sorted(word))].append(word)
        
    return anagrams.values()