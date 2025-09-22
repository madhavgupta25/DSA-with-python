class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def print_linked_list(head:ListNode):
    while head is not None: # better way to check , is keywords is use to compare the address of the object not the value
    # while head != None: # same as above # but we dont recommend to use this
        print(head.val, end=" ")
        head = head.next
    print()
#time : O(1)

def insert_at_head(head,val):
    n = ListNode(val)
    n.next = head
    head = n
    return head

head = None
head = insert_at_head(head, 60)
head = insert_at_head(head, 50)
head = insert_at_head(head, 40)
head = insert_at_head(head, 30)
head = insert_at_head(head, 20)
head = insert_at_head(head, 10)

if head is None:
    print("Yes")

print_linked_list(head) # 10, 20, 30, 40, 50