"""
조건:
enqueue 및 dequeue와 같은 동작을 수행하는 def rotate(self)작성하기.
새로운 메서드는 새로운 노드를 추가하거나 기존 노드를 제거하는 방식이 안됨
즉, 노드 수는 고정.
가장 어려웠던 오류: ~ takes 1 positional argument but 2 were given
해결방법: https://careerkarma.com/blog/python-takes-one-positional-argument-but-two-were-given/

"""
#-----------------------------------------

class LinkedQueue:

    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        self._tail._next = self._head
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        self._tail._next = self._head

    def rotate(self):
        if self._size != 0:
            self._head = self._head._next
            self._tail = self._tail._next

    def printQueue(self):d
        next = self._head
        if self._size != 0:
            while True:
                if next == self._tail:
                    print(next._element, end='')
                    break
                else:
                    print(next._element, end=' ')
                next = next._next
        print(end='')


lq = LinkedQueue()
lq.enqueue(1)
lq.enqueue(3)
lq.enqueue(5)
lq.enqueue(7)
print("Before Rotation: [",end='')
lq.printQueue()
print("]")
lq.rotate()
print("AfterRotation: [",end='')
lq.printQueue()
print("]")

"""
올려주신 과제에서 Q.enqueue(Q.dequeue()) 와 동일한 동작을 구현하면서 클래스 내부의 메서드로
[1, 3, 5, 7]을 삽입하기에 조금의 어려움이 있어 부득이하게
enqueue(e)+rotate()+printQueue()메서드로 나누어 구현하였습니다.
또한 다른 방법인input()메서드를 활용하여 파싱한 뒤 Queue에 삽입하는 경우
__init__메서드의 size 변경이 필요하여 기존 노드의 삭제 또는 새 노드 추가가 발생하기에
최종적으로 LinkedQueue의 내부 메서드 enqueue를 활용하여 element 삽입 후 rotate()메서드로
노드의 위치를 변경한 뒤 printQueue()메서드로 출력하는 방식을 채택하였습니다.
"""
#--------------------------------------------
""" enqueue() 사용이 아닌 input() 일 경우
x = input("Before Rotation: ").replace(" ","")
stripped_x = x.strip("[]")
list_before = stripped_x.split(",")
list_after = list(map(int,list_before))

lq = LinkedQueue(list_after) #코드 error
print("After Rotation: ", lq.rotate())
"""

