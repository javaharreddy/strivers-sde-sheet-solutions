def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            if fast.next.next==slow.next:
                return True
            else:
                slow=slow.next
                fast=fast.next.next
        return False
      
