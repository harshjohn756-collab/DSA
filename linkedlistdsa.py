class Node:
    def __init__(self,data=None,next= None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def printelements(self):
        if self.head is None:
            print("List is empty: ")
            return
        data = self.head
        string = " "
        while data:
            string += str(data.data)+ "--->"
            data = data.next
        print(string)


    def adddata(self,data):
        node = Node(data,self.head)
        self.head = node

    def length(self):
        count=0
        number_of_data = self.head
        while number_of_data:
            count+=1
            number_of_data = number_of_data.next
     
        return count

    def insert_at_end(self,data):
       
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_any_index(self,index,data):
        if index<0 or index > self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.adddata(data)
            return

        count = 1
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count+=1
    def del_tion_fst(self):
        itr = self.head
        self.head = itr.next

    def del_end(self):
        prev = self.head
        nex = prev.next
        while nex.next is not None:
            prev = prev.next
            nex = nex.next
        prev.next = None

    def del_index(self,index):
        if index < 0 or index>self.length():
            raise Exception("Invalid index")
        
        start = self.head
        if index == 0:
            self.head =start.next
            return

        count = 1
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next


            itr = itr.next
            count+=1

    def insert_aftr_value(self,data_after,data_to_insert):
        if self.head is None:
            raise Exception("No element to add")

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data== data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next


    def insert_values(self,data):
        self.head = None
        for da in data:
            self.insert_at_end(da)




ll = linkedList()
ll.adddata(1)
ll.adddata(2)
ll.adddata(3)
ll.adddata(4)
ll.adddata(5)
ll.insert_at_end(6)
ll.insert_any_index(2,1.5)
ll.insert_any_index(4,3.5)
ll.del_tion_fst()
ll.del_end()
ll.del_index(2)
ll.insert_aftr_value(3.5,3.2)
ll.insert_aftr_value(2,2.5)
# ll.insert_values(["Apple","Grapes","Desert"])
ll.printelements()
ll.length()





    

