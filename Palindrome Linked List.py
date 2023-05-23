def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        #reversing the second linkedlist
        headb=slow.next
        temp=headb
        prev=None
        while temp:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        slow=head
        fast=prev
        while fast:
            if slow.val!=fast.val:
                return False
            slow=slow.next
            fast=fast.next
        return True
