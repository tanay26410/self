#circular list
def isCircular(head):
    # Code here
    if head==None:
        return True
    temp=head
    while temp:
        if temp.next==head:
            return True
        temp=temp.next
    return False