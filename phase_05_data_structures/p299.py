class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def has_cycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = b

print(Node.has_cycle(a))
print(Node.has_cycle(Node(1)))