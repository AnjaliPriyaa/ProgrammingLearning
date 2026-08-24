class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Head of linked list
head = node1


# Reverse Linked List
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        # Save next node
        next_node = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_node

    # prev is the new head
    return prev

# Reverse
new_head = reverse_linked_list(head)

# Print Linked List
current = new_head

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")