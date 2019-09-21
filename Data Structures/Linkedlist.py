class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = node

    def display(self):
        ptr = self.head
        if ptr is None:
            print('List is empty')
        else:
            while ptr is not None:
                print(ptr.data, end="-->")
                ptr = ptr.next
            print('None', end='')
        print()

    def count(self):
        ptr = self.head
        co = 0
        while ptr is not None:
            co += 1
            ptr = ptr.next
        return co

    def remove(self, data):
        ptr = self.head
        if ptr is None:
            print('List is empty')
        elif ptr.data == data:
            self.head = ptr.next
        else:
            prev = None
            while ptr is not None and ptr.data != data:
                prev = ptr
                ptr = ptr.next
            if ptr is None:
                print('Data not found')
            else:
                prev.next = ptr.next


sll = LinkedList()

while True:

    try:
        print("1.Append\n2.Count\n3.Display\n4.Remove\n5.Exit\n")
        op = int(input())
        if op == 1:
            data = int(input("Enter data to append : "))
            sll.append(data)
        elif op == 2:
            sll.count()
        elif op == 3:
            sll.display()
        elif op == 4:
            data = int(input("Enter data to remove: "))
            sll.remove(data)
        elif op == 5:
            break
        else:
            print("Invalid option")
    except Exception as e:
        print(e)
