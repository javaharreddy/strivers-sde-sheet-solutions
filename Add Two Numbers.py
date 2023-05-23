def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list=ListNode('x')
        temp=new_list
        carry=0
        while l1 and l2:
            temp.next=ListNode((l1.val+l2.val+carry)%10)
            temp=temp.next
            carry=(l1.val+l2.val+carry)//10
            l1=l1.next
            l2=l2.next
        while l1:
            temp.next=ListNode((l1.val+carry)%10)
            carry=(l1.val+carry)//10
            temp=temp.next
            l1=l1.next
        while l2:
            temp.next=ListNode((l2.val+carry)%10)
            carry=(l2.val+carry)//10
            temp=temp.next
            l2=l2.next
        if carry:
            temp.next=ListNode(carry)
        return new_list.next
