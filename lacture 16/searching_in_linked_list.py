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

# time = O(n)
# sapace = O(1)
def search_linked_list(head:ListNode, target:int) -> bool:
    while head is not None:
        if head.val == target:
            return True
        head = head.next
    return False

head = None # It means linked list is empty
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print_linked_list(head)

target = 30
print(search_linked_list(head, target))