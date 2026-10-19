from collections import defaultdict
from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res={}
        for num in nums:
            res[num]=res.get(num, 0) + 1
        arr=[]
        for num, freq in res.items():  
            arr.append([freq, num])
        
        arr.sort()
        
        sor =[]
        
        while k > len(sor):
            element = arr.pop()
            sor.append(element[1])
            

        return(sor)