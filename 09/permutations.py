def process(left, right, result=[]):
    if len(left) == 0:
        result.append(right)
    else:
        for i in range(len(left)):
            process(left[0:i] + left[i + 1:], [left[i]] + right, result)


def permutations(array):
    result = []
    process(array, [], result)
    return result


# print(permutations(['a', 'b', 'c']))
# print(permutations([1, 2, 3]))
# print(permutations([1]))
# print(permutations([]))
