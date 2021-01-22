class Solution:
    def findLHS(self, nums: List[int]) -> int:
        largest = 0

        for number in sorted(set(nums)):
            print(number)
            newlist = nums.copy()
            newlist = [x for x in newlist if not (x)>(number+1)]
            newlist = [x for x in newlist if not (x)<(number)]
            if max(newlist) - min(newlist) == 1:
                print(newlist)
                if len(newlist) > largest:
                    largest = len(newlist)
                    print("L ",largest)
        return largest
        
