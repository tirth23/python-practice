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

        temp = self.head
        while temp:
            if temp.data == previous_value:
                new_node = Node(new_value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        
        print("No Node found.")

    def append(self, new_value):

        temp = self.head

        if temp == None:
            self.push(new_value)

        while temp:
            if temp.next == None:
                new_node = Node(new_value)
                temp.next = new_node
                return
            temp = temp.next

    def delete(self, value):

        temp = self.head

        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == value:
                prev.next = temp.next
                temp = None
                return
            prev = temp
            temp = temp.next

        if temp == None:
            print("No node to be deleted.")

    def deleteList(self):

        temp = self.head

        if temp == None:
            print("LinkedList is already empty.")

        while temp:
            next_node = temp.next
            self.head = next_node
            temp = None
            temp = next_node

        print("List is deleted.")

    def count(self):

        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        print(f"Node/s present in list are {count}.")

    def reverse(self):

        temp = self.head

        if temp == None:
            print("No linkedlist found to reverse.")

        previous_node = None
        while temp:
            next_node = temp.next
            temp.next = previous_node
            previous_node = temp
            temp = next_node
        self.head = previous_node

    def print(self):

        temp = self.head

        if temp == None:
            print("No linkedlist found which can be printed.")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":

    ll_object = LinkedList()
    ll_object.push(9)
    ll_object.push(8)
    ll_object.push(5)
    ll_object.insert(5, 6)
    ll_object.insert(6, 7)
    ll_object.append(10)
    ll_object.delete(5)
    ll_object.deleteList()
    ll_object.reverse()
    ll_object.count()
    ll_object.append(4)
    ll_object.count()
    ll_object.print()