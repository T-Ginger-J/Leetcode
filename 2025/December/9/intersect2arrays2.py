# LeetCode 350: Intersection of Two Arrays II
# Explanation:
# 1. Count occurrences of elements in nums1.
# 2. For each element in nums2, if it exists in the counter and count > 0:
#    - Add to result
#    - Decrement count
# Time Complexity: O(n + m)
# Space Complexity: O(n)

class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        count1 = Counter(nums1)
        res = []
        for num in nums2:
            if count1.get(num, 0) > 0:
                res.append(num)
                count1[num] -= 1
        return res

print(Solution().intersect([1,2,2,1], [2,2]))      # Output: [2,2]
print(Solution().intersect([4,9,5], [9,4,9,8,4]))  # Output: [4,9] or [9,4]
