def mergeTwoLists(self, temp1: Optional[ListNode], temp2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode('x')
        store=new
        while temp1 and temp2:
            if temp1.val<temp2.val:
                new.next=temp1
                new=new.next
                temp1=temp1.next
            else:
                new.next=temp2
                new=new.next
                temp2=temp2.next
        while temp1:
            new.next=temp1
            new=new.next
            temp1=temp1.next
        while temp2:
            new.next=temp2
            new=new.next
            temp2=temp2.next
        return store.next
