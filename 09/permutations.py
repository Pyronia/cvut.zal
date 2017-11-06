import math


def process(pivot, start_index, array, result):
    result[start_index] = result[start_index] + [pivot]
    passing_array = array.copy()
    passing_array.remove(pivot)
    for pivot in passing_array:
        process(pivot, start_index, passing_array, result)
        start_index += 1


def permutations(array):
    result = []
    for i in range(math.factorial(len(array))):
        result.append([])

    start_index = 0

    for pivot in array:
        process(pivot, start_index, array, result)
        start_index += 1

    print("\npermutations:")
    print(result)
    print(str(start_index))


def permutations_hokus_pokus(head, tail=''):
    result = []

    if len(head) == 0:
        print(tail)
        result.append(list(tail))
    else:
        for i in range(len(head)):
            permutations_hokus_pokus(head[0:i] + head[i+1:], tail+head[i])



# permutations(['a', 'b', 'c'])
permutations_hokus_pokus(['a', 'b', 'c'])
