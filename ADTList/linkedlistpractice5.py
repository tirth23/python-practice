class Node:

    def __init__(self, new_value):
        self.data = new_value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, previous_value, new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp:
            if temp.data == previous_value:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("No node found.")

    def append(self, new_value):
        new_node = Node(new_value)
        temp = self.head
        
        if temp == None:
            self.push(new_value)
        else:
            while temp:
                if temp.next == None:
                    temp.next = new_node
                    return
                temp = temp.next

    def delete(self, value):
        temp = self.head

        if temp.data == value and temp == self.head:
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.data == value:
                prev_node.next = temp.next
                temp = None
                return
            prev_node = temp
            temp = temp.next

    def deleteAll(self):
        temp = self.head
        while temp:
            self.head = temp.next
            temp = None
            temp = self.head
        print("LinkedList is deleted.")

    def reverse(self):
        temp = self.head
        prev = None
        while temp:
            self.head = temp.next
            temp.next = prev
            prev = temp
            temp = self.head
        self.head = prev

    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print(f"Node/s : {count}")

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    def linkListToCircularLinkedList(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = self.head
        print("\nLinkedList converted to CircularLinkedList.")

    def printCircularLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.head:
                break

if __name__ == "__main__":

    llist = LinkedList()
    llist.append(7)
    llist.push(4)
    llist.push(3)
    llist.insert(4, 6)
    llist.insert(4, 5)
    llist.append(8)
    llist.delete(3)
    llist.delete(5)
    #llist.deleteAll()
    #llist.reverse()
    llist.push(1)
    llist.count()
    llist.print()   
    llist.linkListToCircularLinkedList()
    llist.printCircularLinkedList() 