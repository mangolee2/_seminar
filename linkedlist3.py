"""노드 구현"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 다음 노드가 없을 경우, 가르킬 주소가 없다.


"""연결 리스트 구현""" 
class linked_list:
    def __init__(self, data):
        self.head = Node(data)
        

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def search(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next # 주소가 현재 노드가 된다.
        cur.next = Node()

    # 연결리스트 인덱스 
    def get_index(self, index):
        cnt = 0
        node = self.head # 헤더부터 시작
        while cnt < index:
             cnt += 1
             node = node.next
        return node

    # 데이터 삽입
    def insert(self, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_index(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # 데이터 삭제
    def delete(self, length):
        if length == 0:
            self.head = new_node.next
            return
        node = self.get_index(index-1)
        node.next = node.next.next

data = ""                                    
test = linked_list(data)
