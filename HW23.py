######################################################
######################################################
#HW23
#Walter Stepanek
######################################################
######################################################
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

######################################################
######################################################
class linkedList:
    def __init__(self):
        self.head=None

######################################################
    def append(self, data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            lastNode=self.head
            while lastNode.next != None:
                lastNode=lastNode.next
            lastNode.next=newNode

######################################################
    def prepend(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode

######################################################
    def insertAfterNode(self, prevNode, data):
        newNode=Node(data)
        newNode.next=prevNode.next
        prevNode.next=newNode

######################################################
    def printList(self):
        curNode=self.head
        while curNode.next!=None:
            print(curNode.data)
            curNode=curNode.next
        print(curNode.data)

######################################################
    def deleteNode(self,key):
        curNode=self.head
        if curNode!=None and curNode.data==key:
            self.head=curNode.next
            curNode=None
            return
        else:
            prev=None
            while curNode!=None and curNode.data!=key:
                prev=curNode
                curNode=curNode.next
            if curNode==None:
                print('The data is not founf in the list')
                return
            else:
                prev.next=curNode.next
                curNode=None

######################################################
    def deleteAtPos(self,pos):
        curNode=self.head
        if pos==0:
            self.head=curNode.next
            curNode=None
            return
        else:
            cnt=0
            prev=None
            while curNode != None and cnt != pos:
                prev=curNode
                curNode=curNode.next
                cnt+=1
            if curNode==None:
                print("The node doesn't exist")
                return
            else:
                prev.next=curNode.next
                curNode=None

######################################################
    def lenIterative(self):
        cnt=0
        curNode=self.head
        while curNode != None:
            curNode = curNode.next
            cnt+=1
        return cnt

    def lenRecursive(self,headNode):
        if headNode is None:
            return 0
        else:
            return 1+self.lenRecursive(headNode.next)

######################################################
    def swapNode(self,key1,key2):
        if key1==key2:
            print('The two nodes are the same nodes. They cannot be swapped.')
            return
        prev1=None
        curNode1=self.head
        while curNode1 != None and curNode1.data != key1:
            prev1=curNode1
            curNode=curNode1.next
        prev2=None
        curNode2=self.head
        while curNode2 != None and curNode2.data != key2:
            prev2=curNode2
            curNode2=curNode2.next
        if curNode1==None or curNode2==None:
            print("The nodes are not present in the list")
            return
        else:
            if prev1==None:
                self.head=curNode2
                prev2.next=curNode1
            elif prev2==None:
                self.head=curNode1
                prev1.next=curNode2
            else:
                prev1.next=curNode2
                prev2.next=curNode1
            temp1=curNode1.next
            temp2=curNode2.next
            curNode1.next=temp2
            curNode2.next=temp1

######################################################
    def reverseIterative(self):
        prev=None
        curNode=self.head
        while curNode!=None:
            nxtTemp=curNode.next
            curNode.next=prev
            prev=curNode
            curNode=nxtTemp
        self.head=prev


######################################################
######################################################
######################################################
print()
print('Test append function:')
name = linkedList()
name.append('W')
name.append('a')
name.append('l')
name.append('t')
name.append('e')
name.append('r')
name.printList()

#print()
#print('Test prepend function:')
#name.prepend('X')
#name.printList()
#
#print()
#print('Test deleteNode function:')
#name.deleteNode('X')
#name.printList()
#
#print()
#print('Test insertAfterNode function:')
#name.insertAfterNode(name.head.next.next,'X')
#name.printList()

######################################################
######################################################
print()
print('Test deleteAtPos function:')
name.deleteAtPos(3)
name.printList()

print()
print('Test lenIterative function:')
print('The length of the list is', name.lenIterative())

print()
print('Test lenRecursive function:')
print('The length of the list is', name.lenRecursive(name.head))

print()
print('Test swapNode function:')
name.swapNode('W','r')
name.printList()

print()
print('Test reverseIterative funtion:')
name.reverseIterative()
name.printList()
