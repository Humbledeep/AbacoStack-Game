# Humbledeep Singh
# AbacoStack.py 


# Initialisation of Stack class
class Stack:      
    def __init__(self):   # initialisation
        self.items = []
    def push(self, item):       # push function to push in stack
        self.items.append(item)
    def pop(self):        # to pop from stack
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]    # peek function
    def isEmpty(self):
        return self.items == []      # returns True if stack is empty
    def size(self):
        return len(self.items)   # returns size of stack
    def __str__(self):
        
        return(str(self.items))
    def stacks(self,num,Depth_of_Stack):   # initialisaton of stack as a function
        if(num==1):
            return self.items[0:Depth_of_Stack]
        elif(num==2):
            return self.items[Depth_of_Stack:Depth_of_Stack*2]
        else:
            return self.items[Depth_of_Stack*(num-1):Depth_of_Stack*num]
    
    

# Task 1 : The Card Class

class card:   # The card class 
    beads=Stack()
    Num_of_Stacks=0     # initialisations
    Depth_of_Stack=0
    Color=65
    l1=[]
    def __init__(self, size, depth):
        beads=Stack()
        self.Num_of_Stacks= size
        self.Depth_of_Stack= depth
        for s in range(size):
            for d in range(depth):
                #rprint(chr(self.Color))
                self.beads.push(chr(self.Color))
            self.Color=self.Color+1


    def reset(self):
        beads=Stack()  # resetting the stack
        Num_of_Stacks=0
        Depth_of_Stack=0
        Color=65
        
    def stack(self,num):
        li=self.beads.stacks(num,self.Depth_of_Stack)   # appending elements in li list for show
        
        return li

    def show(self):
        #self.l1=[]
        if(not self.l1):
            self.l1.append(self.stack(1))   # function to print the approriate game box and elements
            self.l1.append(self.stack(2))
            self.l1.append(self.stack(3))
        for i in range(len(self.l1)):
            print("|", end="")
            for j in range(len(self.l1[i])):
                print("",self.l1[j][i], end="")
                    
            print("|")


    
# Task 2: The Bounded Stack Class
       

class BStock:
    
    def __init__(self,capacity):  # initialisations with assertions for capacity 
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity >0, ('Error: Illegal capacity: %d' % (capacity))
        self._items=Stack()
        self._capacity=capacity
        
        
    # Returns True if the stack is empty, and False otherwise:
    def isEmpty(self):
        return self._items.size() == 0
    # Returns True if the stack is full, and False otherwise:
    def isFull(self):
        return self._items.size() == self._capacity  # returns true if stack is full
    def push(self,item):
        if self.isFull():  # push function for stack with exception if stack is full
            raise Exception('Error: Stack is full')
        self._items.push(item)
    def show(self):   # show function to print stack items
        print(self._items)


# Task 3: The AbacoStack Class

class AbacoStack:  # AbacoStack class
    def __init__(self,noOfStack,StackDepth):
        self._abacoStack=card(noOfStack,StackDepth)   # Creating Bounding Stack
        self._topList=['.']* (noOfStack+2)     # creating top list  
        
    def print(self):
        #print(map(str,self._topList))
        print('0 1 2 3 4')
        print(*self._topList, sep = ' ')
        self._abacoStack.show()

    def moveBead(self,move):   # movebead function with appropriate actions for appropriate commands
        if(move=='1u'):
            self._topList[1]=self._abacoStack.l1[0][0]
            self._abacoStack.l1[0][0]='.'
                    
           
        elif(move=='1d'):
            self._abacoStack.l1[0][0]=self._topList[1]
            self._topList[1]='.'
        elif(move=='2u'):
            self._topList[2]=self._abacoStack.l1[1][0]
            self._abacoStack.l1[1][0]='.'
        elif(move=='2d'):
            self._abacoStack.l1[1][0]=self._topList[2]
            self._topList[2]='.'
        elif(move=='3u'):
            self._topList[3]=self._abacoStack.l1[2][0]
            self._abacoStack.l1[2][0]='.'
        elif(move=='3d'):
            self._abacoStack.l1[2][0]=self._topList[3]
            self._topList[3]='.'
        elif(move=='0r'):
            self._topList[1]=self._topList[0]
            self._topList[0]='.'
        elif(move=='1r'):
            self._topList[2]=self._topList[1]
            self._topList[1]='.'
        elif(move=='1l'):
            self._topList[0]=self._topList[1]
            self._topList[1]='.'
        elif(move=='2r'):
            self._topList[3]=self._topList[2]
            self._topList[2]='.'
        elif(move=='2l'):
            self._topList[1]=self._topList[2]
            self._topList[2]='.'
        elif(move=='3r'):
            self._topList[4]=self._topList[3]
            self._topList[3]='.'
        elif(move=='3l'):
            self._topList[2]=self._topList[3]
            self._topList[3]='.'
        elif(move=='4l'):
            self._topList[3]=self._topList[4]
            self._topList[4]='.'


    
    def isSolved(self,card):  # function to congratulate user if game is solved
        pass

    def reset(self):
        self._abacoStack=card(noOfStack,StackDepth)   
        self._topList=['.']* (noOfStack+2)     

    def show(self,card):
        self.print()

       
# test data
'''
s=BStock(5)
s.push('A')
s.push('A')
s.push('B')
s.push('B')
s.push('C')
#s.push('C')

s.show()
'''
ab=AbacoStack(3,3)  # calling AbacoStack class and testing the classes

ab.print()

ab.moveBead("1u")
ab.print()
ab.moveBead("1l")
ab.print()
ab.moveBead("2u")
ab.print()
ab.moveBead("2l")
ab.print()
ab.moveBead("1d")
ab.print()


