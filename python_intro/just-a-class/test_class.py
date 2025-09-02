from linked_list import LinkedList

l: LinkedList = LinkedList()
l.append(1)
l.append("Hello")
l.append(None)
l2: LinkedList = LinkedList()
l2.append(4.0)
l.append(l2)
print(l)
