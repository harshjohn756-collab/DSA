class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubleLinkedlist:
    def __init__(self):
        self.head =None

    def transverse(self):
        a = self.head
        while a is not None:
            print(a.data,end=" ")
            a = a.next

    def backward_transverse(self):
        print()
        a = self.head
        while a.next is not None:  
            a = a.next            
        while a is not None:  
              
            print(a.data,end=" ")
            a = a.prev    


    def insert_at_beg(self,data):
        nf = Node(data)
        a = self.head 
        a.prev=nf
        nf.next = a
        self.head = nf  

    def insert_at_end(self,data):
        nl = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = nl
        nl.prev = a  

    def insert_at_specified(self,data,position):
        nm = Node(data) 
        a = self.head
        for i in range(1,position-1):
            a = a.next
        nm.prev = a
        nm.next = a.next
        a.next.prev = nm
        a.next =nm

    def del_at_first(self):
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    def del_at_end(self):
        prev = self.head
        a = prev.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        a.prev = None
    
    def del_at_specific(self,position):
        prev =self.head
        a = prev.next
        for i in range(1,position-1):
            a =a.next                  #n3
            prev = prev.next           #n2
        prev.next = a.next
        a.next.prev = prev
        a.prev = None
        a.next = None
        
n1 = Node(10)
dll = doubleLinkedlist()
dll.head = n1
n2 = Node(20)
n2.prev = n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3
n4 = Node(40)
n4.prev = n3
n3.next = n4
n5 = Node(50)
n4.next = n5

n5.prev = n4



dll.insert_at_beg(5)
dll.insert_at_end(60)
dll.insert_at_specified(25,4)
dll.del_at_first()
dll.del_at_end()
dll.del_at_specific(3)
dll.transverse()

dll.backward_transverse()

lis = [[]for i in range(10)]



lis[2].append(("Harsha.A",31))
lis[2].append(("hb",687))
lis[0].append(("march 6",874))
print(lis)
for element in lis[2]:
    print(element[1])

print(73%10)


