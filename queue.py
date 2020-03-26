# Troy Jeffrey Amegashie
# Queue
# 03/05/2020

from LinkedListTail import LinkedListTail


class Queue:
    def __init__(self):
        self.queue = LinkedListTail()

    def push(self, data):
        self.queue.push_head(data)

    def pop(self):
        self.queue.pop_head()

