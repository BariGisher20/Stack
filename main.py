from typing import Any


class StackItem:
    def __init__(self, value: Any, prev_stack_item: 'StackItem' = None):
        self.value = value
        self.prev_stack_item = prev_stack_item


class Stack:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        if self.tail is None:
            return True
        else:
            return False

    def push(self, value: Any):
        new_stack_item = StackItem(value, self.tail)
        self.tail = new_stack_item
        return self

    def pop(self, value: Any):
        value = self.tail.value
        self.tail = self.tail.prev_stack_item
        return value

    def peek(self):
        value = self.tail
        if self.isEmpty():
            return 'Пустой'
        return value.value

    def __iter__(self):
        self.cursor = StackItem(None, self.tail)
        return self

    def __next__(self):
        if self.cursor.prev_stack_item is None:
            raise StopIteration
        self.cursor = self.cursor.prev_stack_item

    def size(self):
        counter = 0
        for i in self:
            counter += 1
        return counter


open = ['(', '[', '{']
close = [')', ']', '}']


def check(str):
    stack = Stack()
    for i in str:
        if i in open:
            stack.push(i)
        elif i in close:
            if open.index(stack.peek()) == close.index(i):
                stack.pop(stack.peek())

    if stack.isEmpty():
        return 'ok'
    else:
        return 'not ok'


str_1 = '{[}]'
print(check(str_1))