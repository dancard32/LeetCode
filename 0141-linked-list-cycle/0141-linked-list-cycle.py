# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize data
        seen = set()
        cur = head
        
        # Loop through the list
        while cur:
            
            # If seen before
            if cur in seen: return True
            seen.add(cur)
            cur = cur.next
        
        # Else
        return False