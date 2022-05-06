
def extensionFinder(fileName):
    extension = fileName.split(".")
    print("Output: " +extension[-1])


fileName = input("Enter your file name: ")
extensionFinder(fileName)