class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create nodes
node1 = Node(3)
node2 = Node(15)
node3 = Node(17)
node4 = Node(90)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4  

head = node1  # Head points to the first node

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


current = head
print("Old LL:", end=" ")

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")


# -------- REVERSE --------

new_head = reverse_linked_list(head)


# -------- PRINT NEW LIST --------

current = new_head

print("New LL:", end=" ")

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")