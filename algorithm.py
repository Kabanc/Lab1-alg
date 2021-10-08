from stack import Stack

OPERATORS = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
FUNCTIONS = ["sin", "cos"]


def infix2postfix(line):
    output = ""
    ops = Stack()

    tokens = line.split(" ")
    for token in tokens:
        if token.isnumeric():
            output += token + " "
        elif token in FUNCTIONS:
            ops.push(token)
        elif token in OPERATORS:
            output += _handleOp(token, ops)
        elif token == '(':
            ops.push(token)
        elif token == ')':
            output += _handleCloseBracket(ops)

    while not ops.isEmpty():
        output += ops.pop() + " "

    return output.rstrip()


def _handleOp(op1, ops):
    output = ""

    while True:
        if ops.isEmpty() or ops.top() not in OPERATORS:
            ops.push(op1)
            return output

        op2 = ops.top()

        if OPERATORS[op2] > OPERATORS[op1] or (OPERATORS[op2] == OPERATORS[op1] and op1 != '^'):
            output += ops.pop() + " "
        else:
            ops.push(op1)
            return output


def _handleCloseBracket(ops):
    output = ""
    while str(ops.top()) != '(':
        if not ops.isEmpty():
            output += ops.pop() + " "
        else:
            raise EOFError("Не совпадает количество открывающихся и закрывающихся скобок")

    ops.pop()

    if not ops.isEmpty() and ops.top() in FUNCTIONS:
        output += ops.pop() + " "

    return output
