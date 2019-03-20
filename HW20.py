#HomeWork 20
#Walter Stepanek

'''
1.

Understand the Stack datastructure and use it to solve the 'divided by two',
'reverse a string', and the 'parenthesis balance check' problems by yourself.

(Understand the solutions in the tutorial first and then type it out,
use Vim, by yourself).

(possible quiz/exams in the future on this will be close-book,
close-notes, and close-internet problems).

(without looking at the solution,
use Vim to type these out for as many times as you can,
until you can get it right independently).

Upload your code to your GitHub account and
send the link of the repository to the homework email.
'''
class Stack:
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

##Divided by two
baseTen = 256 #This number can be changed for different outputs
printIn = baseTen
s=Stack()
binary=''
while baseTen>0:
    r = baseTen%2
    baseTen = baseTen//2
    s.push(r)
while not s.is_empty():
    binary += str(s.pop())

print('The decimal number %s is %s in binary' % (printIn, binary))

##Reverse a string
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
reverse = ''
for x in string:
    s.push(x)
while not s.is_empty():
    reverse += str(s.pop())
print('The alphabet backwards is: %s' % reverse)

##Parenthesis balance check
def parMatch(p1, p2):
    if p1=='(' and p2==')':
        return True
    elif p1=='[' and p2==']':
        return True
    elif p1=='{' and p2=='}':
        return True
    else:
        return False

def is_par_bal(parString):
    index = 0
    is_bal = True
    s = Stack()
    if parString == '':
        is_bal = False
        return False
    if parString[-1] in '{[(':
        is_bal = False
        return False
    else:
        while index<len(parString) and is_bal==True:
            if parString[index] in '{[(':
                s.push(parString[index])
            else:
                if s.is_empty():
                    is_bal = False
                    return False
                elif parMatch(s.pop(), parString[index]):
                    is_bal = True
                else:
                    is_bal==False
                    return False
            index += 1
        if not s.is_empty():
            return False
        if s.is_empty() and is_bal==True:
            return True

print(is_par_bal('[]'))
print(is_par_bal('([{}])'))
print(is_par_bal('(([)'))
print(is_par_bal('())'))
print(is_par_bal('))'))
print(is_par_bal('(('))
print(is_par_bal(''))
print(is_par_bal('()[]{}'))

