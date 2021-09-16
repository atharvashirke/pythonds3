from stack import Stack

def postfix(infix_string):
    """
    Converts infix string to postfix
    """
    prec = {"**": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    op_stack = Stack()
    output = []
    infix_string = infix_string.split()
    print(infix_string)
    for item in infix_string:
        if item in prec:
            if item == "(":
                op_stack.push(item)
            else:
                while not op_stack.is_empty() and prec[item] <= prec[op_stack.peek()]:
                    output.append(op_stack.pop())
                op_stack.push(item)
        elif item == ")":
            while op_stack.peek() != "(":
                output.append(op_stack.pop())
        else:
            output.append(item)
    while not op_stack.is_empty():
        if op_stack.peek() == "(":
            op_stack.pop()
        else:
            output.append(op_stack.pop())
    return ' '.join(output)

def postfix_eval(postfix_string):
    """
    Evaluates a postfix string and returns an integer
    """
    operators = ["*", "/", "+", "-"]
    operand_stack = Stack()
    postfix_string = postfix_string.split()
    for item in postfix_string:
        if not item in operators and not item.isdigit():
            raise RuntimeError(f"Invalid item {item} in input")
        if item.isdigit():
            operand_stack.push(int(item))
        if item in operators:
            if item == "*":
                operand_stack.push(operand_stack.pop() * operand_stack.pop())
            elif item == "/":
                divisor = operand_stack.pop()
                operand_stack.push(operand_stack.pop() // divisor)
            elif item == "+":
                operand_stack.push(operand_stack.pop() + operand_stack.pop())
            elif item == "-":
                    operand_stack.push(operand_stack.pop() - operand_stack.pop())
    return operand_stack.pop()




def main():
    choice = input("Enter 0 for infix -> postfix conversion. Enter 1 for postfix evaluation: ")
    if choice == "0":
        string = input("Write an infix expression you'd like to convert: ")
        print(postfix(string))
    elif choice == "1":
        string = input("Write a postfix expression of integers you'd like to evaluate: ")
        print(postfix_eval(string))
    else:
        raise RuntimeError("Invalid choice. Please choose from given options.")

main()
