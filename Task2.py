

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return(str(self.items))
    def stacks(self,num,Depth_of_Stack):
        if(num==1):
            return self.items[0:Depth_of_Stack]
        elif(num==2):
            return self.items[Depth_of_Stack:Depth_of_Stack*2]
        else:
            return self.items[Depth_of_Stack*(num-1):Depth_of_Stack*num]

class BStock:
    _items=Stack()
    def __init__(self,capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity >0, ('Error: Illegal capacity: %d' % (capacity))
        #self._items=Stack()
        self._capacity=capacity
        
        
    
    def isEmpty(self):
        return self._items.size() == 0
    # Returns True if the stack is full, and False otherwise:
    def isFull(self):
        return self._items.size() == self._capacity
    def push(self,item):
        if self.isFull():
            raise Exception('Error: Stack is full')
        self._items.push(item)
    def show(self):
        print(self._items)


s=BStock(5)
s.push('A')
s.push('A')
s.push('B')
s.push('B')
s.push('C')
s.show()

