class Node:
    def __init__(self, key, value):
        self.data = [key, value]
        self.next = None


class LRUCache:
    def __init__(self):
        self.front = None
        self.rear = None
        self.capacity = 0
        self.miss = 0
        self.hit = None
        self.getList = []
        self.references = 0

    
    def put(self, key, value):
        if 0<=key<=100 and 0<=value<=100:
            self.references += 1
            if self.checking(key) == -1:
                if self.capacity != 50:
                    
                    
                    if self.front == None:
                        self.front = Node(key, value)
                        self.rear = self.front
                        self.capacity += 1
                        self.miss += 1
                        return "Added Successfully!!!!!"

                    newNode = Node(key, value)
                    self.rear.next = newNode     
                    self.rear = self.rear.next
                    self.capacity+=1
                    self.miss+= 1
                    return "Updated Cache!"
                

                elif self.capacity == 50:
                    self.front = self.front.next
                    self.rear.next = Node(key, value)
                    self.rear =  self.rear.next
                    self.miss +=1

            else:
                self.updateValue(key,value)
        else:
            print("The key or value should be between 0 - 100")    

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
            
    
    def get(self, key):
        self.references += 1
        key = key 
        getValue = self.checking(key)
        if getValue != -1:
            print(f"The value of the key: {key} is {getValue}")
            self.rear.next = Node(key, getValue)
            self.rear = self.rear.next
            a = self.front
            b = a.next
            if a is not None and a.data[0] == key:
                self.front = b
                return
            
            while b is not None:
                if b.data[0] == key:
                    a.next = b.next
                    return
                a = a.next
                b = b.next

        else:
            self.miss += 1
            print(-1)
            return
                

        
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

    def calculateMiss(self):
        print(f"Miss = {self.miss}")
        print(f"References = {self.references}")
        x = int((self.miss/self.references)*100)
        print(f"The Miss Rate is {x}%")
        y = 100 - x
        print(f"The Hit Rate is {y}%")


print("                                                          *******************************  ")
print("                                                          * Welcome To LRUCache Program *  ")
print("                                                          *******************************  ")







userInput = input("Enter c to conitnue......... ").lower()
if userInput == "c":
    # obj1 = LRUCache()
    # obj1.put(1,'a')
    # obj1.put(2,'b')
    # obj1.put(3,'c')
    # obj1.traverse()
    # obj1.put(1,'k')
    # obj1.traverse()
    # obj1.put(6,'m')
    # obj1.put(8,'l')
    # obj1.traverse()
    # obj1.put(6,'v')
    # obj1.traverse()
    # obj1.put(8,'n')
    # obj1.traverse()
    # obj1.get(3)
    # obj1.traverse()
    # obj1.get(8)
    # obj1.traverse()
    # obj1.get(9)
    # x = obj1.miss/obj1.references
    
    # print(x)
    cache = LRUCache()
    for i in range(50):
        cache.put(i, i)

    for i in range(1,101,2):
        cache.get(i)

    for i in range(101):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            cache.put(i,i)
    cache.calculateMiss()
    cache.traverse()



















    

            



    




