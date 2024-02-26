# Humbledeep Singh


# Stack class from AbacoStack.py
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
    
    

# Task 1 (Card Class) from AbacoStack.py
class card:        
    beads=Stack()
    Num_of_Stacks=0
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
        beads=Stack()
        Num_of_Stacks=0
        Depth_of_Stack=0
        Color=65
        
    def stack(self,num):
        li=self.beads.stacks(num,self.Depth_of_Stack)
    
        return li

    def show(self):
        
        if(not self.l1):
            self.l1.append(self.stack(1))
            self.l1.append(self.stack(2))
            self.l1.append(self.stack(3))
        for i in range(len(self.l1)):
            print("|", end="")
            for j in range(len(self.l1[i])):
                print("",self.l1[j][i], end="")
                    
            print("|")


 # Bounded class from AbacoStack.py       
class BStock:
    
    def __init__(self,capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity >0, ('Error: Illegal capacity: %d' % (capacity))
        self._items=Stack()
        self._capacity=capacity
        
        
    # Returns True if the stack is empty, and False otherwise:
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

# Abacostack class from AbacoStack.py
class AbacoStack:
    def __init__(self,noOfStack,StackDepth):
        self._abacoStack=card(noOfStack,StackDepth)   # Creating Bounding Stack
        self._topList=['.']* (noOfStack+2)     # crating top list  
        
    def print(self):
        #print(map(str,self._topList))
        print('0 1 2 3 4')
        print(*self._topList, sep = ' ')
        self._abacoStack.show()

    def moveBead(self,move):
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


    
    def isSolved(self):   
        solvedcard=[['A','B','C'],['A','C','B'],['C','A','B']]
        
        if (len(self._abacoStack.l1) != len(solvedcard)):
            return False
        
         
        # Linearly compare elements
        for i in range(0, len(solvedcard) - 1):
            if (self._abacoStack.l1[i] != solvedcard[i]):
                return False
         
        # If all elements were same.
        return True

    def reset(self,noOfStack,StackDepth):
        self._abacoStack=card(noOfStack,StackDepth)   
        self._topList=['.']* (noOfStack+2)     

    def show(self,card):
        self.print()

    
# Task 4: The Game

StackSize=int(input("Enter Stack Size Between (2 to 5):"))    # Game inputs 
Stackdepth=int(input("Enter Stack Depth Between(2 to 4):"))

stackcard=AbacoStack(StackSize,Stackdepth)  # calling AbacoStack class

stackcard.print()

movelist=['1u','1d','2u','2d','3u','3d','0r','1r','1l','2r','2l','3r','3l','4l']  # valid moves list

while(not stackcard.isSolved()): # until game is not solved
    moves=input("Enter Your Moves (one or Five Moves At once )(Q for Quit and R to reset) :")
    if(moves=="q" or moves=="Q"):
        print("Thanks For Playing !!!!")  # quit command
        quit()
    elif(moves=="r" or moves=="R"):  # reset command
        stackcard.reset(StackSize,Stackdepth)
        stackcard.print()
    else:
        m=moves.split()
        
        for s in m:
            if(not s in movelist):
                raise Exception('Error: Invalid Move')  # moves not in list exception raised
            else:
                stackcard.moveBead(s)
                stackcard.print()
            
            




