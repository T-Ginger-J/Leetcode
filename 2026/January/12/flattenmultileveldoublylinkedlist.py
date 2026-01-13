# LeetCode 430: Flatten a Multilevel Doubly Linked List
# Explanation:
# 1. Use DFS to traverse nodes recursively.
# 2. If a node has a child, flatten the child list and insert it between the node and node.next.
# 3. Keep track of the tail of the flattened child list to connect back to the main list.
# 4. Set child pointers to None after flattening.

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        def dfs(node: 'Node') -> 'Node':
            curr = node
            last = node  # keep track of the last node in the flattened list
            
            while curr:
                next_node = curr.next
                if curr.child:
                    # Flatten child and get the tail
                    child_last = dfs(curr.child)
                    
                    # Insert the child between curr and next_node
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None
                    
                    if next_node:
                        child_last.next = next_node
                        next_node.prev = child_last
                    
                    last = child_last
                else:
                    last = curr
                
                curr = next_node
            return last
        
        dfs(head)
        return head

