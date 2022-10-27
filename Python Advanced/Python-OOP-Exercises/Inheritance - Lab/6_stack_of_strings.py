
class Stack:
    data = []

    def push(self, element):
        if isinstance(element, str):
            Stack.data.append(element)

    def pop(self):
        return Stack.data.pop()

    def top(self):
        return Stack.data[-1]

    def is_empty(self):
        if Stack.data:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(Stack.data[::-1])}]"




