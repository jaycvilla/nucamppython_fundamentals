class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)


dllist = DoublyLinkedList()
dllist.append("First Node")




"""
Terminal commands

$ python -i linked_list4.py
Head Node created: First Node
>>> dllist.head.value
'First Node'
>>> dllist.tail.value 
'First Node'
>>> dllist.append("Second Node")
Appended new Node with value: Second Node
>>> dllist.head.value 
'First Node'
>>> dllist.tail.value 
'Second Node'
>>> dllist.head.next.value 
'Second Node'
>>> dllist.tail.prev.value 
'First Node'
>>> dllist.head.prev.value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'value'
>>> dllist.tail.next.value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'value'
>>> dllist.append("Third  Node") 
Appended new Node with value: Third  Node
>>> dllist.tail.value            
'Third  Node'
>>> dllist.tail.prev.value 
'Second Node'
>>> dllist.tail.prev.prev.value 
'First Node'
>>> dllist.head.next.next.value 
'Third  Node'
"""