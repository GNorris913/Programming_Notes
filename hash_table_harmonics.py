class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        largestKey = 0
        largest = 0
        hashmap = {}
        
        for number in set(nums):
            hashmap[number] = 0
            
        for number in nums:
            hashmap[number] = hashmap[number]+1
            
        print(sorted(hashmap.keys()))
        for key in sorted(hashmap.keys()):
            print(key)
            nextkey = int(key+1)
            if nextkey in hashmap.keys():
                length = hashmap[key] + hashmap[nextkey]
                print("length ", length)
                print("largest", largest)
                if largest < length:
                    largest = length
                    print("l=l ",largest)
                    largestKey = key
        
        print("lk ",largestKey)
        return largest

"""
Best Hashmap Result from leetcode user FACEPLANT

h, result = {}, []
for num in nums:
	h[num] = h.get(num, 0) + 1
for k in h.keys():
	if h.get(k + 1):
		result = max(result, h[k] + h[k + 1])
return result
"""
