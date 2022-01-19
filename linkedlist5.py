class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class linked_list: # 노드들의 연결
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    # pos 번째의 node를 가리키고 싶을 때 쓰는 메서드
    def get_at(self, pos):
        if pos <= 0 or pos > self.node_count: # 특정 경우 예외 처리
            return None
        
        i = 1
        cur = self.head 

        while i < pos:
            cur = cur.next
            i += 1
        return cur
    
    # 순회
    def traverse(self):
        t_list = []
        cur_node = self.head # 첫 노드에 접근

        while cur_node != None: # tail이 되면 None이 됨
            t_list.append(cur_node.data) # 노드가 아니라 data 입력
            cur_node = cur_node.next # 다음 노드에 접근

        return t_list


 # 위 코드 선형배열, 보완
    def insert3(self, pos, new_node):
        if pos < 0 or pos > self.node_count:
            return False

        if pos == 0:
            new_node.next = self.head
            self.head = new_node

        # prev 를 미리 지정
        else: # prev 를 tail 로 지정
            if pos == self.node_count + 1:
                prev = self.tail
                self.tail = new_node
            else: # prev 를 들어갈 자리(pos)의 바로 전 자리로 지정
                prev = self.get_at(pos-1)
            new_node.next = prev.next # 뒤 연결
            prev.next = new_node # 앞 연결
        
        self.node_count += 1 # 추가 후 노드 갯수 증가
        return True
        # 맨 앞 십입/ 맨 끝 삽입 : O(1), 중간 삽입: O(n)


 # 맨 앞, 맨 뒤를 제거할 때, 유일한 리스트 원소를 제거할 때 처리불가 보완
    def delete2(self, pos):
        if pos < 0 or pos > self.node_count:
            raise IndexError
        cur = self.get_at(pos) # 제거할 노드

        if self.node_count == 1 & pos == 0: # 유일한 리스트
            self.head = None
            self.tail = None

        elif pos == 0:
            self.head = self.get_at(pos+1) # 유일하지 않지만 맨 앞 삭제
            
        else:
            prev = self.get_at(pos-1)

            if self.node_count != pos:
                prev.next = self.get_at(pos+1) # 맨 뒤가 아닐 때
            else:
                self.tail = prev # 맨 뒤 삭제
                prev.next = None

        self.node_count -= 1
        return cur.data


exc = linked_list()

print(exc)
a = Node(10)
exc.insert3(0,a)
