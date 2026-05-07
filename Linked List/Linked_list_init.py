class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    head = a
    a.next = b
    b.next = c
    c.next = d

    curr = head
    while curr:
        print(curr.data)
        curr = curr.next