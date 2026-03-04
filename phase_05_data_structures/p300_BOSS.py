class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delete(self, val):
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.val == val:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

    def search(self, val):
        current_node = self.head
        while current_node:
            if current_node.val == val:
                return True
            current_node = current_node.next
        return False
    
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    
    def reverse(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=' ')
            current_node = current_node.next
        print()

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()
ll.delete(2)
ll.display()
print(ll.search(3)) 
ll.reverse()
ll.display()
print(ll.has_cycle()) 
