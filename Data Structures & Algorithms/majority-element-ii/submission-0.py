class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
            
            if len(hashmap) <= 2:
                continue

            new_count = defaultdict(int)
            for n, c in hashmap.items():
                if c > 1:
                    new_count[n] = c - 1
            
            count = new_count

        res = []
        for num in hashmap:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res
