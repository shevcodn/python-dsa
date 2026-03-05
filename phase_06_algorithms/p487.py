class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

def make_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

print(find_middle(make_list([1, 2, 3, 4, 5])))
print(find_middle(make_list([1, 2, 3, 4])))
print(find_middle(make_list([1])))