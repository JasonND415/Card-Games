class Stack:
    def __init__(self):
        self.items=[]
        self.count=0
    def push(self,l):                      #add item
        self.items.append(l)
        self.count+=1                      #increase size
    def pop(self):
        self.count-=1                       #decrease size when popping
        if self.count==-1:                  #raise Error if 0 items
            raise IndexError("Can't pop from empty stack")
        return self.items.pop()
    def size(self):
        return self.count                    #get size of stack
    def isEmpty(self):
        if self.count==0:                    #if size is 0, return true isEmpty
            return True
        else:                                #else return false
            return False
    def peek(self):
        if self.count==0:                    #if peeking into empty stack, then raise error
            raise IndexError("Can't peek in empty stack")
        return self.items[len(self.items)-1]   #else return