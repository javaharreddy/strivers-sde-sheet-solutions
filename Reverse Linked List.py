def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            temp=head
            prev=None
            while temp:
                cur=temp.next
                temp.next=prev
                prev=temp
                temp=cur
            return prev
