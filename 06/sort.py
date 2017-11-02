# Machiavelli: "Divide and rule", Quick sort
def sortNumbers(weights, condition):
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

            return sortNumbers(left, condition) + center + sortNumbers(right, condition)

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

            return sortNumbers(left, condition) + center + sortNumbers(right, condition)

        else:
            return weights

    else:
        raise ValueError('Invalid input data')


def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError('Invalid input data')

    leftW = []
    centerW = []
    rightW = []

    leftD = []
    centerD = []
    rightD = []

    if condition == 'ASC':
        if len(data) > 1:
            pivot = weights[0]
            for i in range(len(data)):
                if pivot > weights[i]:
                    leftW.append(weights[i])
                    leftD.append(data[i])
                elif pivot == weights[i]:
                    centerW.append(weights[i])
                    centerD.append(data[i])
                else:
                    rightW.append(weights[i])
                    rightD.append(data[i])

            return sortData(leftW, leftD, condition) + centerD + sortData(rightW, rightD, condition)

        else:
            return data

    elif condition == 'DESC':
        if len(data) > 1:
            pivot = weights[0]
            for i in range(len(data)):
                if pivot < weights[i]:
                    leftW.append(weights[i])
                    leftD.append(data[i])
                elif pivot == weights[i]:
                    centerW.append(weights[i])
                    centerD.append(data[i])
                else:
                    rightW.append(weights[i])
                    rightD.append(data[i])

            return sortData(leftW, leftD, condition) + centerD + sortData(rightW, rightD, condition)

        else:
            return data

    else:
        raise ValueError('Invalid input data')


def runTests():
    result = sortNumbers([4, 2, 3], 'ASC')
    expected = [2, 3, 4]
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('sortNumbers([4, 2, 3], \'ASC\'), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')

    result = sortNumbers([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'ASC')
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('sortNumbers([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], \'ASC\'), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')

    result = sortNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'DESC')
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('sortNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], \'ASC\'), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')

    result = sortData([2, 5, 6], ['Ford', 'BMW', 'Audi'], 'ASC')
    expected = ['Ford', 'BMW', 'Audi']
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('sortData([2,5,6], [\'Ford\', \'BMW\', \'Audi\'], \'ASC\'), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')


runTests()
