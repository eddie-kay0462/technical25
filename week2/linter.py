class Stack:
    def __init__(self) -> None:
        self.items  = []

    #push to the stack
    def push(self, item):
        self.items.append(item)

    #pop from the stack 
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
    
    #read from the stack   
    def read(self):
        if not self.items:
            return None
        return self.items[-1]
    
class Linter:
    def __init__(self) -> None:
        self.stack = Stack()

    def lint(self, text):
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)
            elif self.is_closing_brace(char):
                popped_opening_brace  = self.stack.pop()
                print(f"Popped {popped_opening_brace}")
                if not popped_opening_brace:
                    return f"{char} does not have an opening brace"
                if self.is_not_a_match(popped_opening_brace, char):
                    return f"{char} has a mismatched opening brace"
        if self.stack.read():
            return f"{self.stack.read()} does not have closing brace"


        return True        




    def is_opening_brace(self, char):
        return char in "({["
    
    def is_closing_brace(self, char):
        return char in ")]}"
    
    def is_not_a_match(self, opening_brace, closing_brace):
        pairs = {"(": ")", "[": "]", "{": "}"}
        return pairs.get(opening_brace) != closing_brace
    


linter = Linter()
# print(linter.lint("({[]})"))  # True
# print(linter.lint("({[})"))   # } has mismatched opening brace
# print(linter.lint("({[}"))    # } has mismatched opening brace
# print(linter.lint("({["))     # [ does not have closing brace
print(linter.lint("])"))      # ] doesn't have opening brace