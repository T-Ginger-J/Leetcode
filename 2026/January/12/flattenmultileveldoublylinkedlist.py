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

