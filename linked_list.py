class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def __str__(self):
        if self.first != None:
            current = self.first
            out = '[' + str(current.value)
            while current.next != None:
                current = current.next
                out += ', ' + str(current.value)
            return out + ']'
        return 'LinkedList []'
    def __len__(self):
        return self.length
    def append(self, x):
        self.length+=1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)
    def pop(self,i):
        if (self.first == None):
            return
        curr = self.first
        self.length -= 1
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                   self.last = curr
                old.next = curr.next 
                break
            old = curr  
            curr = curr.next
            count += 1
l=LinkedList()
for i in range(10):
    l.append(i)
print(l)
print(len(l))
l.pop(0)
print(l)
print(len(l))