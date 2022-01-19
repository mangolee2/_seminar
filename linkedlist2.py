"""노드 구현"""
from dataclasses import dataclass


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None # 다음 노드가 없을 경우, 가르킬 주소가 없다.

"""연결 리스트 구현"""       
class linked_list:
    def __init__(self):
        self.head = Node()

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def search(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next # 주소가 현재 노드가 된다.
        cur.next = Node()
   
    # 연결리스트 인덱스 
    def get_node(self, index):
        cnt = 0
        node = self.head # 헤더부터 시작
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    # 삽입
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        new_node.next = next_node

    # 삭제
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next

                                                                                                                  
