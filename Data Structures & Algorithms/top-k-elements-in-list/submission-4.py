class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        for num in nums:
            res[num]=res.get(num, 0) + 1
            
        buckets = [[]for _ in range(len(nums)+1 )]
        
        
        for num,freq in res.items():
            buckets[freq].append(num)
            
        answ = []
        while len(answ) <k:
            current_bucket = buckets.pop()
            if current_bucket:
                for num in current_bucket:
                    answ.append(num)
        return (answ[:k])
