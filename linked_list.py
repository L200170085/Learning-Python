class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.start_node = None

    def traverse_list(self) :
        if self.start_node is None :
            print ("List has no element.")
            return
        else :
            n = self.start_node
            while n is not None :
                print(n.data, " ")
                n = n.next
                
    #menambah data pada posisi awal
    def insert_at_start(self, data) :
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node

    #menambah data pada posisi akhir
    def insert_at_end(self, data) :
        new_node = Node(data)
        if self.start_node is None :
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None :
            n = n.next
        n.next = new_node
        
    #menambah data setelah posisi yang dipilih
    def insert_after_item(self, choose, data) :
        n = self.start_node
        print (n.next)
        while n is not None :
            if n.data == choose :
                break
            n = n.next
        if n is None :
            print ("Item not in the list.")
        else :
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    #menambah data sebelum posisi yang dipilih
    def insert_before_item (self, choose, data) :
        if self.start_node is None :
            print ("List has no element.")
            return

        if choose == self.start_node.data :
            new_node = Node(data)
            new_node.next = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.next)
        while n.next is not None :
            if n.next.data == choose :
                break
            n = n.next

        if n.next is None :
            print ("item not in the list.")
        else :
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    #menambahkan data pada posisi yang diinginkan
    def insert_at_index(self, index, data) :
        if index == 1 :
            new_node = Node(data)
            new_node.next = self.start_node
            self.start_node = new_node

        i = 1
        n = self.start_node
        while i < index-1 and n is not None :
            n = n.next
            i = i + 1

        if n is None :
            print ("Index out of bound")
        else :
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    #menghitung jumlah elemen pada linked list
    def get_count(self):
        if self.start_node is None :
            return 0

        n = self.start_node
        count = 0
        while n is not None :
            count = count + 1
            n = n.next
        return count

    #mencari elemen pada linked list
    def search_item(self, x) :
        if self.start_node is None :
            print ("List has no elements.")
            return

        n = self.start_node
        while n is not None :
            if n.data == x :
                print ("Item found.")
                return True
            n = n.next
        print ("Item not found.")
        return False

    #membuat linked list berdasarkan inputan, berupa berapa panjang linked list-nya dan element apa saja yang disimpan.
    def make_new_list(self) :
        nums = int(input("How many nodes do you want to create : "))
        if nums == 0 :
            return

        for i in range (nums) :
            value = int(input("Enter the value for the node : "))
            self.insert_at_end(value)

    #menghapus element pada linked list
    def delete_element_by_value(self, x):
        if self.start_node is None :
            print ("The list has no element to delete.")
            return

        if self.start_node.data == x :
            self.start_node = self.start_node.next
            return

        n = self.start_node
        while n.next is not None :
            if n.next.data == x :
                break
            n = n.next

        if n.next is None :
            print ("Item not found in the list.")
        else :
            n.next = n.next.next
            
##dlist = LinkedList()
##dlist.insert_at_end(5)
##dlist.insert_at_end(10)
##dlist.insert_at_end(15)
##dlist.insert_at_start(20)
##dlist.insert_at_index(3, 7)
##dlist.traverse_list()


