"""Solucion base para brackets problem
"""

from Estructuras.Stack import Stack

def brackets_pair(s: str)->str:
    if s==")":
        return "("
    elif s=="]":
        return "["
    return "{"

def validate_program(program: str) -> str:
    brackets_stack = Stack()

    for i, char in enumerate(program):
        if (char == "(") or (char == "[") or  (char == "{"): 
            brackets_stack.push((char, i))

        elif (char == ")") or (char == "]") or  (char == "}"):
            if brackets_stack.is_empty():
                return f"{char} {i}"

            top_char = brackets_stack.pop()
            pair = brackets_pair(char)

            if pair != top_char[0]:
                return f"{char} {i}"
    
    return "ok so far"

def main():
    _ = 19
    programa = "[[]] () ) [] {{}} {"

    print(validate_program(programa))

if __name__ == "__main__":
    main()