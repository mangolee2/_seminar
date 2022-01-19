
class Node:
    def __init__(self):
        self.prev = None
        self.data = []
        self.next = None


class cal:
    def __init__(self, data):
        self.headNode = Node()
        self.headNode.data = data
        self.tailNode = self.headNode
        self.nodeCnt = 1
    def search(self, data, order):
        '''
        반환 : 데이터랑 비교해서 해당 노드를 반환함
        '''
        curNode = ""
        if order == True:
            curNode = self.headNode
            while(True):
                if curNode.next == None:
                    return "no data"
                if curNode.data == data:
                    return curNode
                curNode = curNode.next

        else:
            curNode = self.tailNode
            while(True):
                if curNode.prev == None:
                    return "no data"
                if curNode.data == data:
                    return curNode
                curNode = curNode.prev

        

    def delete(self, data, order):
        delObject =  self.search(data, order)
        if delObject == self.headNode:
            curNode = delObject.next
            self.headNode = curNode
            curNode.prev = None
        
        if delObject == self.tailNode:
            curNode = delObject.prev
            self.prevNode = curNode
            curNode.next = None

        preNode =  delObject.prev
        nextNode = delObject.next
        preNode.next = nextNode
        nextNode.prev = preNode


    def insert(self, num, order,data):
        '''
        어디에 노드를 넣을지
        '''
        addNode = Node()
        self.nodeCnt += 1
        if num > self.nodeCnt:
            return "노드의 길이가 짧습니다."
        addNode.data = data
        if order == True:

            curNode = self.headNode
            for i in range(num):
                curNode = curNode.next
            if curNode == self.tailNode:
                preNode = curNode
                addNode.prev = preNode
                preNode.next = addNode
                self.tailNode = addNode
                return

            if curNode == self.headNode:
                nextNode = curNode.next
                addNode.next = nextNode
                nextNode.prev = addNode
                self.headNode = addNode
                return
            
                

            preNode = curNode.prev
            nextNode = curNode.next
            addNode.prev = preNode
            addNode.next = nextNode
            preNode.next = addNode
            nextNode.prev = addNode


factory = cal(10)
print(factory)
factory.insert(0, True, 10)
print(factory.headNode.next.data)
factory.insert(1, True, 10)
print(factory.headNode.next.next.data)
print(factory.tailNode.prev.prev.prev)
factory.delete(10, True)