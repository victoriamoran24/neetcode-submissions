class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        frequence = defaultdict(set)

        for n in nums:
            if n not in counter: 
                counter[n] += 1
                frequence[1].add(n)

            else: 
                count = counter[n]
                frequence[count].remove(n)
                frequence[count + 1].add(n)
                counter[n] += 1
        
        ordered = []

        for count in frequence:
            ordered.extend(frequence[count])

        return ordered[len(ordered) - k:]
            