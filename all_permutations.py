## ALL PERMUTATIONS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perList = []
        self.permutations(nums=nums, perlist=perList)
        print(perList)
        return perList

    def permutations(self, nums=[], itemp=[], perlist=[], index=0):
        temp = itemp.copy()
        print(f"index: {index}, nums {nums}")
        if not nums:
            perlist.append(temp)
            print(perlist)
        else:
            for number in nums:
                temp = itemp.copy()
                print(f"number {number}")
                temp.append(number)
                tnums = nums.copy()
                tnums.remove(number)
                self.permutations(nums=tnums, itemp=temp, perlist=perlist, index=index + 1)
