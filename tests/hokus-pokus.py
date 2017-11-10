def hokus(array):
    kontrola = True

    while kontrola:
        kontrola = False
        for i in range(len(array)):
            if i < len(array) - 1:
                if array[i] > array[i+1]:
                    gnom = array[i+1]
                    array[i+1] = array[i]
                    array[i] = gnom
                    kontrola = True

    return array


print(hokus([2, 5, 4, 1, 3]))
