class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(current.data, end=" -> ")
        current = current.next
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        if not self.head:
            print("The linked list is empty.")
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"The middle node is {slow.data}.")
        return slow     
li = LinkedList()
li.append(10)
li.append(20)
li.append(30)
li.append(40)
li.append(50)
li.find_middle_node()