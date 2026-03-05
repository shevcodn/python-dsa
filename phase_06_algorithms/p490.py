class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return
    
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev

    first = head
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

def make_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

head = make_list([1,2,3,4,5])
reorder_list(head)
print(to_list(head))

head2 = make_list([1,2,3,4])
reorder_list(head2)
print(to_list(head2))