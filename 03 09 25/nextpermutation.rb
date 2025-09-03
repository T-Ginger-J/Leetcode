class Solution
  def next_permutation(nums)
    i = nums.length - 2

    # Step 1: Find first decreasing element from the end
    while i >= 0 && nums[i] >= nums[i + 1]
      i -= 1
    end

    if i >= 0
      j = nums.length - 1
      # Step 2: Find element just larger than nums[i]
      while nums[j] <= nums[i]
        j -= 1
      end
      nums[i], nums[j] = nums[j], nums[i]
    end

    # Step 3: Reverse the tail
    left = i + 1
    right = nums.length - 1
    while left < right
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1
    end
  end
end
