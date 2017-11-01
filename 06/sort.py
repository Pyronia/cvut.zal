# Machiavelli: "Divide and rule", Quick sort
def sortNumbersBeforeRefactoring(weights, condition):
    left = []
    center = []
    right = []

    if condition == 'ASC':
        if len(weights) > 1:
            pivot = weights[0]
            for element in weights:
                if pivot > element:
                    left.append(element)
                elif pivot == element:
                    center.append(element)
                else:
                    right.append(element)

            return sortNumbersBeforeRefactoring(left, 'ASC') + center + sortNumbersBeforeRefactoring(right, 'ASC')

        else:
            return weights

    elif condition == 'DESC':
        if len(weights) > 1:
            pivot = weights[0]
            for element in weights:
                if pivot < element:
                    left.append(element)
                elif pivot == element:
                    center.append(element)
                else:
                    right.append(element)

            return sortNumbersBeforeRefactoring(left, 'DESC') + center + sortNumbersBeforeRefactoring(right, 'DESC')

        else:
            return weights

    else:
        raise ValueError('Invalid input data')


def sortNumbers(weights, condition):
    left = []
    center = []
    right = []

    if len(weights) > 1:
        pivot = weights[0]
        for element in weights:
            if pivot > element:
                left.append(element)
            elif pivot == element:
                center.append(element)
            else:
                right.append(element)

        return sortNumbers(left, condition) + center + sortNumbers(right, condition)

    else:
        return weights


def sortData(weights, data, condition):
    pass



def runTests():
    result = sortNumbers([4, 2, 3], 'ASC')
    expected = [2, 3, 4]
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('sortNumbers([4, 2, 3], \'ASC\'), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')


runTests()
