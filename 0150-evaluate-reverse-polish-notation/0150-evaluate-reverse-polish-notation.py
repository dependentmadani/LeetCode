def make_the_operations(operator, value1, value2):
    result = 0

    if (operator == '*'):
        result = int(value1) * int(value2)
    elif (operator == '/'):
        result = int(int(value1) / int(value2))
    elif (operator == '+'):
        result = int(value1) + int(value2)
    elif (operator == '-'):
        result = int(value1) - int(value2)

    return result

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        array_of_operations = []

        operators = ['*', '/', '+', '-']
        for i in tokens:
            if i not in operators:
                array_of_operations.append(i)
            else:
                result = make_the_operations(i, array_of_operations[len(array_of_operations) - 2], array_of_operations[len(array_of_operations) - 1])
                array_of_operations.pop()
                array_of_operations.pop()
                array_of_operations.append(result)
            
        return int(array_of_operations[0])
