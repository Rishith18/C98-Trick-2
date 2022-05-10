def swapFileData():
    file1 = input("Enter you file here:")
    file2="sample2.txt"

    a = open(file1, 'r')
    data_a = a.read()

    b = open(file2, 'r')
    data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

    print(data_a)
swapFileData()