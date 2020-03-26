# Troy Jeffrey Amegashie
# Stack
# 03/05/2020

from LinkedLists import LinkedList


class Stack:
    def __init__(self):
        self.mystack = []

    def push(self,data):
        self.mystack.append(data)

    def pop(self):
        return self.mystack.pop()


