def writeTextToFile(suffix):
    prefix = 'This is my static text which must be added to file. ' \
             'It is very long text and I do not know what they want to do with this terrible text. '
    # cast to string
    suffix = str(suffix)
    filename = "myFirstFile.txt"
    file = open(filename, 'w')
    file.write(prefix + suffix)
    file.close()
    return filename

writeTextToFile("Hello")
writeTextToFile(123)

