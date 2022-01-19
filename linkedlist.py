
class Node:
    def __init__(self):
        self.prev = None
        self.data = []
        self.next = None

class cal:
    def __init__(self):
        self.headNode = Node()
        self.tailNode = ""
        # self.nodeCnt = 1


    def insert(self, node, order):
        addNode = Node()
        if order == True:
        if num > self.nodeCnt:
            return "너무 길어요"
        if order == True:
            currentNode = self.headNode
            for i in range(num):
                currentNode = currentNode.next
                if currentNode == self.tail:
                    self.tail.next =  
                
            


            if num == self.nodeCnt:

                num.next = self.nodeCnt 
                self.nodeCnt.prev = num
        else:




            
    def search(self, node, order):
        
        if order == True:
            currentNode = self.headNode
            while(True):
                if node == currentNode.data:
                    break
                

                currentNode = currentNode.next
                if currentNode == self.tailNode:
                    break
        else:
            currentNode = self.tailNode
            while(True):
                if node == currentNode.data:
                    break

                currentNode = currentNode.prev
                if currentNode == self.headNode:
                    break
        return currentNode.data
    
        
a = Node()
b = Node()
c = Node()

a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = a



# print(a.data)
            