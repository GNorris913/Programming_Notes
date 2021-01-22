class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        newnum = self.reduceify(num, k)
        newnum = newnum.lstrip("0")
        if newnum == "": return '0'
        else: return newnum
    
    def reduceify(self, num, k):
        
        if len(num) == k: return "0"
        if k > 0:
            for char in range(len(num)-1):
                if int(num[char]) > int(num[char+1]):
                    #remove largest left
                    if char > 0:
                        num = num[:char]+ num[char+1:]
                    else: num = num[1:]
                    return self.reduceify(num,k-1)
            #if it doesn't get a hit: remove last int
            return self.reduceify(num[:-1],k-1)
        #return num if k < 1
        return num
        
        #While K or num > 0
        #for char in num, if i > i+, remove.
        #if no catch, remove last number
        
        
        
        
        
        """
        Plan: [x] > [x+1]
        
        Gotchas:
            All the same
            Leading 0's
            Last char bigger
            k = num
            returning null
        
        
        Test cases:
        1111 : 1
        0000 : 1
        123 : 3     = 0
        112 : 1     = 11
        100 : 1
        10 : 1
        968462 : 3 = 642
        """