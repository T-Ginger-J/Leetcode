class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                # x > second → triplet found
                return True

        return False
