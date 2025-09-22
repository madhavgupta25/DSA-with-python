class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
def print_linked_list(head:ListNode):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

def insert_at_head(head,val):
    n = ListNode(val)
    n.next = head
    head = n
    return head

def delete_at_head(head):
    if head is None:
        return None
    
    head = head.next
    return head

def get_tail(head):
    while head.next is not None:
        head = head.next
    return head
    
def insert_at_tail(head,val):
    if head is None:
        head = insert_at_head(head,val)
        return head
    
    n = ListNode(val)
    tail = get_tail(head)
    tail.next = n
    return head
    
    # time = O(n)
    #space = O(1)
def delete_at_tail(head):
    if head is None:
        # this means linked list is empty
        return None
    
    if head.next is None:
        # this means linked list has only one element so head = tail
        head = delete_at_head(head)
        return head
    
    prev = None
    curr = head
    
    while curr.next is not None:
        prev=curr
        curr = curr.next
    
    prev.next = None
    
    return head
    
head = None
head = insert_at_head(head,50)
head = insert_at_head(head,40)
head = insert_at_head(head,30)
head = insert_at_head(head,20)
head = insert_at_head(head,10)

print_linked_list(head)

head = delete_at_head(head) # delete one element
print_linked_list(head)

head = insert_at_tail(head,100)
print_linked_list(head)
        
head = delete_at_tail(head)
print_linked_list(head)