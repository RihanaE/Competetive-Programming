class MyLinkedList(object):

    def __init__(self):
        self.linked_list = []

    def get(self, index):
        if index not in range(len(self.linked_list)):
            return -1
        return self.linked_list[index]
        

    def addAtHead(self, val):
        self.linked_list = [val] + self.linked_list 
        

    def addAtTail(self, val):
        self.linked_list.append(val)
        

    def addAtIndex(self, index, val):
        if index in range(len(self.linked_list)):
            self.linked_list = self.linked_list[:index] + [val] + self.linked_list[index:]
        elif index == len(self.linked_list):
            self.addAtTail(val)
        
        

    def deleteAtIndex(self, index):
        if index in range(len(self.linked_list)):
            self.linked_list = self.linked_list[:index] + self.linked_list[index+1:]
            
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
