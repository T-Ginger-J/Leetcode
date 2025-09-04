class Solution
  def search_range(nums, target)
    first = find_bound(nums, target, true)
    return [-1, -1] if first == -1
    last = find_bound(nums, target, false)
    [first, last]
  end

  private

  def find_bound(nums, target, is_first)
    left = 0
    right = nums.length - 1
    bound = -1

    while left <= right
      mid = (left + right) / 2
      if nums[mid] == target
        bound = mid
        if is_first
          right = mid - 1  # search left half
        else
          left = mid + 1   # search right half
        end
      elsif nums[mid] < target
        left = mid + 1
      else
        right = mid - 1
      end
    end

    bound
  end
end
