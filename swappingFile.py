def swapFileData():
    data_a = input("Enter the File Name: ")
    data_b = input("Enter the File Name: ")

    with open(sample1.txt, 'r') as a:
        data_a = a.read

    with open(sample1.txt, 'w') as a:
        a.write(data_b)


    with open(sample2.txt, 'r') as a:
        data_b = b.read

    with open(Sample2.txt, 'r') as a:
        b.write(data_b)