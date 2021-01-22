class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #print("NUMS ",nums)
        net_sum = sum(nums)
        modulus = net_sum % p
        #print("MODULUS ",modulus)
        if not modulus:
            print("RETURN 0")
            return 0
        
        for window in range(1,len(nums)):
            for index in range(len(nums)+1-window):
                #print(nums[index:index+window])
                post_sum =sum(nums[index:index+window])
                #print(post_sum)
                
                #if modulus == sum(nums[index:index+window]):
                if not (net_sum - post_sum) % p:
                    print("RETURN", window)
                    return window
        print("RETURN -1")
        return -1
        
