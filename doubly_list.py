class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList(object):
    def __init__(self):
        self.head = None

    def traverse_list(self) :
        if self.head is None :
            print ("List has no element")
            return
        else :
            n = self.head
            while n is not None :
                print (n.data, " ")
                n = n.next
        
    def insert_in_emptylist(self, new_data) :
        if self.head is None :
            new_node = Node(new_data)
            self.head = new_node
        else :
            print ("List is not empty")

    def insert_at_end(self, new_data) :
        if self.head is None :
            new_node = Node(new_data)
            self.head = new_node
            return

        n = self.head
        while n.next is not None :
            n = n.next
        new_node = Node(new_data)
        n.next = new_node
        new_node.prev = n

    def insert_after_item(self, x, new_data) :
        if self.head is None :
            print ("List is empty")
            return

        else :
            n = self.head
            while n is not None :
                if n.data == x :
                    break
                n = n.next
            if n is None :
                print ("item not in the list")
            else :
                new_node = Node(new_data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None :
                    n.next.next = new_node
                n.next = new_node

    def insert_before_item(self, x, new_data) :
        if self.head is None :
            print ("List is empty")
            return
        else :
            n = self.head
            while n is not None :
                if n.data == x :
                    break
                n = n.next

            if n is None :
                print ("item not in the list")
            else :
                new_node = Node(new_data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None :
                    n.prev.next = new_node
                n.prev = new_node

    def delete_at_start(self):
        if self.head is None :
            print ("The list has no element to delete")
            return

        if self.head.next is None :
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self) :
        if self.head is None :
            print ("The list has no element to delete")
            return

        if self.head.next is None :
            self.head = None
            return

        n = self.head
        while n.next is not None :
            n = n.next
        n.prev.next = None


    def delete_element_by_value(self, x):
        if self.head is None :
            print ("The list has no element to delete")
            return

        if self.head.next is None :
            if self.head.data == x :
                self.head = None
            else :
                print ("Item not found")
            return

        n = self.head
        while n.next is not None :
            if n.data == x :
                break
            n = n.next

        if n.next is not None :
            n.prev.next = n.next
            n.next.prev = n.prev
        else :
            if n.data == x :
                n.prev.next = None
            else :
                print ("Element not found")
                
d2 = doublyLinkedList()
d2.insert_at_end(10)
d2.insert_at_end(12)
d2.insert_at_end(14)
d2.insert_at_end(16)
d2.insert_after_item(16, 8)
d2.insert_before_item(8, 18)

