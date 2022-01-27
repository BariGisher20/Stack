from typing import Any


class StackItem:
    def __init__(self, value: Any, prev_stack_item: 'StackItem' = None):
        self.value = value
        self.prev_stack_item = prev_stack_item


class Stack:
    def __init__(self):
        self.tail = None

    def __isEmpty__(self):
        if self.tail is None:
            return True
        else:
            return False

    def push(self, value: Any):
        new_stack_item = StackItem(value, self.tail)
        self.tail = new_stack_item

    def pop(self):
        self.tail = self.tail.prev_stack_item.value
        return self.tail

    def peek(self):
        value = self.tail.value
        return value

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


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(5)
    my_stack.push(3)
    my_stack.push(2)
    print(my_stack.size())
