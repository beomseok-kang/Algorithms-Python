class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1): # 절반만 연산 (힙)
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i): # 부모 노드 인덱스 찾기
        if i & 1: # i가 홀수일 경우 (1과 비트가 겹치지 않는다.)
            return i >> 1 # i/2 (1비트만큼 오른쪽으로 옮기면 /2가 됨, 나머지 생략)
        else: # i가 짝수일 경우
            return (i >> 1) - 1 # i/2 -1

    def left_child(self, i): #자식 노드 인덱스 찾기
        return (i<<1) + 1 # 2i+1 (1비트만큼 왼쪽으로 옮기면 *2가 됨)
    def right_child(self, i):
        return (i<<1) + 2 # 2i+2
    
    def __max_heapify__(self, i):
        largest = i # 현재 노드 인덱스
        left = self.left_child(i) # 왼쪽 자식 노드 인덱스
        right = self.right_child(i) # 오른쪽 자식 노드 인덱스
        n = len(self.data)

        # 왼쪽 자식 노드 먼저 계산한다.
        # 먼저 왼쪽 노드가 존재하는지부터 확인.
        # 그 후 왼쪽 노드와 부모 노드 (현재 노드) 의 값을 비교한다.
        # 만약 true라면 (왼쪽 노드가 부모 노드보다 큰 값이라면), largest에 왼쪽 노드의 인덱스를 넣는다.
        # 만약 false라면, or 뒤의 i (부모 노드의 인덱스 값) 의 값을 largest에 넣는다.
        largest = (left < n and self.data[left] > self.data[i]) and left or i
        largest = (right < n and self.data[right] > self.data[largest]) and right or largest

        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i] # 자리 교체
            self.__max_heapify__(largest) # 재귀 함수, 계속해서 반복
    
    def extract_max(self):
        n = len(self.data)
        # 내보낼 값 저장 (가장 큰 값)
        max_element = self.data[0]
        # 첫 번째 노드에 마지막 노드를 삽입
        self.data[0] = self.data[n-1]
        # 마지막 노드 제거 후 재정렬
        self.data = self.data[:n-1]
        self.__max_heapify__(0)
        return max_element
    
    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i != 0 ) and item > self.data[self.parent(i)]:
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        self.data[i] = item
    
l1 = [3,2,5,1,7,8,2]

h = Heapify(l1)
if h.extract_max() == 8:
    print('테스트 통과!')

        
        