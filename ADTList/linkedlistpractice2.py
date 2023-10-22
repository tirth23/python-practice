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

    def insert(self, prev_value, new_value):
        temp = self.head

        while temp:
            if temp.data == prev_value:
                new_node = Node(new_value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        
        print("No node found having such value.")

    def append(self, new_value):
        temp = self.head

        if temp == None:
            self.push(new_value)
            return

        while temp.next:
            temp = temp.next

        new_node = Node(new_value)
        temp.next = new_node

    def delete(self, value):
        temp = self.head

        if temp != None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        
        if temp != None:
            while temp:
                if temp.data == value:
                    prev.next = temp.next
                    temp = None
                    return        
                prev = temp
                temp = temp.next

        if temp == None:
            print("List is empty.")
                
    def deleteAll(self):
        temp = self.head

        while temp:
            nxt = temp.next
            del temp.data
            temp = nxt

        print("List is deleted.")

    def countnode(self):
        temp = self.head

        count = 0
        while temp:
            count += 1
            temp = temp.next

        return count

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()

    ll.push(5)
    ll.append(6)
    ll.insert(5, 7)
    ll.push(8)
    ll.append(9)
    ll.insert(9, 10)
    ll.delete(8)
    #ll.deleteAll()
    ll.print()
    print(ll.countnode())