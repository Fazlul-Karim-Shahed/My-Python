
def firstLastFinder(list):
    list = list.split(",")
    firstItem = list[0]
    lastItem = list[-1]
    print("First item: " + firstItem + " Last item " + lastItem)

list = input("Enter comma seperated numbers: ")

firstLastFinder(list)