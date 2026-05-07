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

def insertAtEnd(data):
    global head
    nn = Node(data)
    if head is None:
        head = nn
    else:
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = nn

def insertAt(data, pos):
    global head
    nn = Node(data)
    if not head:
        head = nn
    else:
        cur = head
        i = 0
        while i < pos-1 and cur and cur.next:
            cur = cur.next
            i += 1
        nn.next = cur.next
        cur.next = nn

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
