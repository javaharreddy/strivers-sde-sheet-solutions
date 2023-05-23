def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cycle=False
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                cycle=True
                break
        if cycle:
            temp=head
            while temp!=slow:
                temp=temp.next
                slow=slow.next
            return temp
        return None
        
