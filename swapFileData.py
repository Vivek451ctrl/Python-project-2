def swapFileData():
    fileName = input("enter the file name:")

    f = open(fileName, 'r')

    with open("ok.txt", 'r') as a:
        data_a = a.read()

    with open("hello.txt", 'r') as a:
        data_b = a.read()

    with open("ok.txt", 'w') as a:
        a.write(data_b)

    with open("hello.txt", 'w') as a:
        a.write(data_a)

swapFileData()