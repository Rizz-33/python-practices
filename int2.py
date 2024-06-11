myList = []

listLenght = int(input("Enter the length of the list "))

def postNumbers(listLenght):
    print("Enter ", listLenght, " number of elements")
    for i in range(0, listLenght):
        element = float(input())
        myList.append(element)
    return myList

def calculation(listLenght):
    total = 0
    for i in range(0, listLenght):
        total = total + myList[i]
    return total/listLenght

postNumbers(listLenght)

print("Average : ",calculation(listLenght))
