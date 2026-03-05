class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

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

print(to_list(remove_nth_from_end(make_list([1, 2, 3, 4, 5]), 2)))
print(to_list(remove_nth_from_end(make_list([1]), 1)))
print(to_list(remove_nth_from_end(make_list([1, 2]), 1)))