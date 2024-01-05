class Node:
    def __init__(self, key, value):
        self.data = [key, value]
        self.next = None


class LRUCache:
    def __init__(self):
        self.front = None
        self.rear = None
        self.capacity = 0
        self.miss = None
        self.hit = None
        self.getList = []

    
    def put(self, key, value):
        if self.checking(key) == -1:
            if self.capacity != 3:
                
                
                if self.front == None:
                    self.front = Node(key, value)
                    self.rear = self.front
                    self.capacity += 1
                    return "Added Successfully!!!!!"

                newNode = Node(key, value)
                self.rear.next = newNode     
                self.rear = self.rear.next
                self.capacity+=1
                return "Hello World"
            

            elif self.capacity == 3:
                self.front = self.front.next
                self.rear.next = Node(key, value)
                self.rear =  self.rear.next

        else:
            self.updateValue(key,value)

    def updateValue(self,key,value):
        a = self.front
        if a.data[0] == key:
            a.data[1] = value
            return

        while a is not None:
            if a.data[0] == key:
                a.data[1] = value
                return
            a = a.next
            
    # def realTimeUpdate(self):

            

    
    def get(self, key):
        key = key 
        getValue = self.checking(key)
        print(f"The value of the key: {key} is {getValue}")
        self.rear.next = Node(key, getValue)
        self.rear = self.rear.next
        self.front = self.front.next


        
    def checking(self, key):
        a = self.front
        
        while a is not None:
            if a.data[0] == key:
                return a.data[1]
            a = a.next
        return -1
    

    def traverse(self):
        a = self.front
        while a is not None:
            print(f"{a.data[0]} = {a.data[1]}", end=" -> ")
            a = a.next
        print("None")


obj1 = LRUCache()
obj1.put(1,'a')
obj1.put(2,'b')
obj1.put(3,'c')
obj1.traverse()
obj1.put(1,'k')
obj1.traverse()
obj1.put(6,'m')
obj1.put(8,'l')
obj1.traverse()
obj1.put(6,'v')
obj1.traverse()
obj1.put(8,'n')
obj1.traverse()
obj1.get(3)
obj1.traverse()
obj1.get(8)
obj1.traverse()

    

            



    




