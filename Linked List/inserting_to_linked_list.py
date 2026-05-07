from Linked_list_init import Node

head = None

def insertAtTop(data):
    global head
    nn = Node(data)
    if head is None:
        head = nn
    else:
        nn.next = head
        head = nn

def travelers():
    cur:Node = head
    while cur is not None:
        print(cur.data)
        cur = cur.next

insertAtTop("A")
insertAtTop("B")
insertAtTop("C")
insertAtTop("D")
insertAtTop("E")

print(travelers())
