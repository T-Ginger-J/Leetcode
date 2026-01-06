# Definition for singly-linked list
class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, _next = nil)
    @val = val
    @next = _next
  end
end

class Solution
  def remove_nth_from_end(head, n)
    dummy = ListNode.new(0, head)
    slow = dummy
    fast = dummy

    # Move fast ahead by n+1 steps
    (n + 1).times do
      fast = fast.next
    end

    # Move both pointers until fast reaches the end
    while fast
      slow = slow.next
      fast = fast.next
    end

    # Remove nth node
    slow.next = slow.next.next

    dummy.next
  end
end

# Helper function to build linked list from array
def build_list(arr)
  dummy = ListNode.new
  curr = dummy
  arr.each do |val|
    curr.next = ListNode.new(val)
    curr = curr.next
  end
  dummy.next
end

# Helper function to print linked list
def print_list(head)
  while head
    print "#{head.val} "
    head = head.next
  end
  puts
end

# Example usage
head = build_list([1, 2, 3, 4, 5])
solution = Solution.new
new_head = solution.remove_nth_from_end(head, 2)
print_list(new_head) # Output: 1 2 3 5
