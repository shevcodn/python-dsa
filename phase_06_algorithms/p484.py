class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def make_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


print(to_list(reverse_list(make_list([1, 2, 3, 4, 5]))))
print(to_list(reverse_list(make_list([1, 2]))))
print(to_list(reverse_list(make_list([]))))
