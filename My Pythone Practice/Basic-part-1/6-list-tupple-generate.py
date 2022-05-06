
def listTupleGenerator(number):
    list = number.split(",")
    tupple = tuple(list)
    print(list)
    print(tupple)

numbers = input("Input numbers with comma: ")

listTupleGenerator(numbers)
