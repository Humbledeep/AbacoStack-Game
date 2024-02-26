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
    
    


class card:
    beads=Stack()
    Num_of_Stacks=0
    Depth_of_Stack=0
    Color=65
    def __init__(self, size, depth):
        self.Num_of_Stacks= size
        self.Depth_of_Stack= depth
        for s in range(size):
            for d in range(depth):
                #rprint(chr(self.Color))
                self.beads.push(chr(self.Color))
            self.Color=self.Color+1


    def reset(self):
        pass

    def show(self):
        print(self.beads)

    def stack(self,num):
        print(self.beads.stacks(num,self.Depth_of_Stack))
            

c=card(3,3)

c.show()
c.stack(1)
c.stack(2)
c.stack(3)


    
