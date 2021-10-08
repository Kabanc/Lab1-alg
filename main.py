from algorithm import infix2postfix
from stack import Stack
from arr import Array
from list import List

if __name__ == "__main__":
    newList = List()

    newList.add(10)
    newList.add(20)
    newList.add(228)
    newList.add(1)
    print(newList)

    newList.add(50)
    print(newList)

    newList.remove(20)
    print(newList)

    newArray = Array()

    newArray.add(10)
    newArray.add(20)
    newArray.add(30)
    print(newArray)

    newArray.set(2, 50)
    print(newArray)

    newArray.remove(10)
    print(newArray)

    newStack = Stack()
    newStack.push(10)
    newStack.push(20)
    newStack.push(30)
    newStack.push(40)
    print(newStack)
    newStack.pop()
    print(newStack)

    print(infix2postfix("10 + sin ( 20 ) - cos ( 30 * 4 ) ^ 5"))
    print(infix2postfix("( 1 + 2 ) * 3"))
    print(infix2postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"))
    print(infix2postfix("0 + 1 * ( 2 ^ 3 - 4 ) ^ ( 5 + 6 * 7 ) - 8"))
    print(infix2postfix("sin ( cos ( 2 ) / 3 * 4 )"))
