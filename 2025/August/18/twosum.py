class Solution(object):
    def twoSum(self, nums, target):
        #dictionary tracks list
        seen = {}
        #iterate through list
        for i, num in enumerate(nums):
            #find pair
            complement = target - num
            #look if pair exists in list
            if complement in seen:
                #return list of the two indexes
                return [seen[complement], i]
            #store number with its index in dictionary
            seen[num] = i

    