class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



class MyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    ## GET ##
    def get(self, index: int) -> int:
        if not self.is_element_index(index):
            return -1
        
        p = self.head.next

        for _ in range(index):
            p = p.next
        return p.val

    def get_first(self, index: int) -> int:
        if self.size < 1:
            raise IndexError("No elements in the list")
        return self.head.next.val
    
    def get_last(self, index: int) -> int:
        if self.size < 1:
            raise IndexError("No elements in the list")
        
        return self.tail.prev.val

    
    def addAtHead(self, val: int) -> None:
        x = Node(val)
        successor = self.head.next
        
        # Link x between head and the old first node
        x.prev = self.head
        x.next = successor
        
        # Update head and old first node to point to x
        self.head.next = x
        successor.prev = x
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        predecessor = self.tail.prev
        
        # Link new node 
        new_node.next = self.tail
        new_node.prev = predecessor
        
        # Update neighbors
        predecessor.next = new_node
        self.tail.prev = new_node
        
        self.size += 1


        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == self.size:
            self.addAtTail(val)
            return

        p = self.head.next
        for _ in range(index):
            p = p.next

        prev = p.prev
        x = Node(val)

        prev.next = x
        x.prev = prev

        x.next = p
        p.prev = x

        self.size += 1

    
    def deleteFirst(self) -> None:
        target =  self.head.next
        temp = target.next

        self.head.next = temp
        temp.prev = self.head

        # Clean
        target = None

        self.size-=1

    def deleteLast(self) -> None:
        target = self.tail.prev
        temp = target.prev

        self.tail.prev = temp
        temp.next = self.tail

        # Clean
        target = None
        self.size-=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        p = self.head.next

        for _ in range(index):
            p = p.next
        
        prev = p.prev
        nxt = p.next

        prev.next = nxt
        nxt.prev = prev

        self.size-=1

        

    ## Helper Methods
    def is_element_index(self, index):
        return 0 <= index < self.size
    
    def is_position_index(self, index):
        return 0 <= index <= self.size

    def check_element_index(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")





















# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)