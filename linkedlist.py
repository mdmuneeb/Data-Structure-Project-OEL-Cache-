
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


#     def listIntoLinkedList(self, lst):
#         self.head = Node(lst[0])
#         current = self.head

#         for i in range(1,len(lst)):
#             current.next = Node(lst[i]) 
#             current = current.next                  

#     def traverse(self):
#         current = self.head
#         i=0
#         while current is not None:
#             print(f"Node {i} -> {current.data}")
#             i+=1
#             current = current.next
    
#     def insert(self, value):
#         n = Node(value)
#         n.next = self.next
#         self.next = n


# lst = [4, 2, 3, 4, 5, 6, 4, 8, 9, 4]
# a= Node(lst[0])
# a.listIntoLinkedList(lst)
# a.insert('a')
# a.traverse()


class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traverse(self):
        a=self
        print("Traversing the list...")
        while a is not None:
            print(a.data,end=" ")
            a=a.next

    def __len__(self):
        a = self
        i=0
        while a is not None:
            i+=1
            a = a.next
        return i

    def insert(self, value):
        n = ListNode(value)
        n.next=self.next
        self.next=n

    def delete(self):
        item=None
        if self.next is not None:
            tmp=self.next
            item=tmp.data
            self.next=tmp.next
        return item

    def search(self,target):
        a=self
        if a.data==target:
            return [True, None, a]
        b=a.next
        while b is not None and b.data!=target:
            a=a.next
            b=b.next
        return [b is not None, a, b]
